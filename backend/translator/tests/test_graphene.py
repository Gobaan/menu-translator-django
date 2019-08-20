import json
import pytest

from backend.schema import schema
from model_mommy import mommy

pytestmark = pytest.mark.django_db

@pytest.fixture()
def user(db):
    annotations = [mommy.make('Annotation')]
    yield mommy.make('UserProfile', annotations=annotations)

@pytest.fixture()
def image(db):
    yield mommy.make('Image')

@pytest.fixture()
def food(db):
    yield mommy.make('Food')

def get_nth_node(content, n=0):
    return content['edges'][n]['node']

def test_images(image):
    query_string = '''
      query getImageInfo
      {
        allImages {
          edges
          {
            node {
              filesize
            }
          }
        }
      }
    '''
    response = schema.execute(query_string, op_name='getImageInfo')
    assert not response.errors
    first_node = get_nth_node(response.data['allImages'])
    assert first_node['filesize'] == image.filesize

def test_foods(food):
    query_string = '''
      query getFoodInfo
      {
        allFoods {
          edges
          {
            node {
              name
            }
          }
        }
      }
    '''
    response = schema.execute(query_string, op_name='getFoodInfo')
    assert not response.errors
    first_node = get_nth_node(response.data['allFoods'])
    assert first_node['name'] == food.name


def test_users(user):
    query_string = '''
    query getUserInfo
    {
      allUsers {
        edges
        {
          node {
            annotations 
            {
              edges {
                node { 
                  text
                }
             }
           }
         }
        }
      }
    }
     '''
    response = schema.execute(query_string, op_name='getUserInfo')
    assert not response.errors
    first_node = get_nth_node(response.data['allUsers'])
    first_annotation = get_nth_node(first_node['annotations']) 
    assert first_annotation['text'] == user.annotations.all()[0].text

def test_user_no_password(user):
    query_string = '''
      query getUserInfo
      {
        allUsers {
          edges
          {
            node {
              password
            }
          }
        }
      }
    '''
    response = schema.execute(query_string, op_name='getUserInfo')
    assert response.errors
    assert response.errors[0].message == 'Cannot query field "password" on type "UserNode".'

def test_user_no_base_access(user):
    query_string = '''
      query getUserInfo
      {
        allUsers {
          edges
          {
            node {
              user {
                id
              }
            }
          }
        }
      }
    '''
    response = schema.execute(query_string, op_name='getUserInfo')
    assert response.errors
    message = response.errors[0].message
    assert message == 'Cannot query field "user" on type "UserNode".'

def test_create_image(user):
    query_string = '''
      mutation ($someFile: Upload!){
        createImage(picture: $someFile, longitude:10, latitude:30) {
          image { 
            id
            filesize
            cloudUrl
          }
        }
      }
    '''
    variable_files = {'someFile': open("TODO.txt")}
    response = schema.execute(query_string, 
        op_name='createImage', 
        variables=variable_files)
    assert not response.errors
    assert response.data['createImage']['image']['filesize'] == 50
