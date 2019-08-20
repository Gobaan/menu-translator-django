set nocompatible              " be iMproved, required
filetype off                  " required

"set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
so ~/.vim/plugins.vim

filetype plugin indent on    " required
filetype plugin on

:color desert
let g:ale_linter_aliases = {'vue': ['vue', 'javascript']}
let g:ale_linters = {'python': ['pycodestyle', 'pylint', 'flake8', 'mypy']}
let g:ale_fixers = {
\ '*': [ 'remove_trailing_lines', 'trim_whitespace'],
\ 'python': [ 'add_blank_lines_for_python_control_statements', 'autopep8', 'black', 'isort', 'reorder-python-imports','yapf'],
\ 'javascript': [ 'eslint' ],
\ }
let g:ale_fix_on_save = 1
map <C-o> :NERDTreeToggle<CR>
set laststatus=2

let g:lightline = {
      \ 'colorscheme': 'seoul256',
      \ }

if !has('gui_running')
    set t_Co=256
endif

set incsearch
set noshowmode
set paste
nmap <C-n> :NERDTreeToggle<CR>
set tabstop=4 shiftwidth=4 expandtab
nmap <F8> :TagbarToggle<CR>


" Enable folding
set foldmethod=indent
set foldlevel=99
" Enable folding with the spacebar
nnoremap <space> za

map  f <Plug>(easymotion-bd-f)
nmap f <Plug>(easymotion-overwin-f)

:autocmd BufRead *.py Coveragepy show
:autocmd BufWritePost *.py Coveragepy refresh
let g:indentLine_color_term = 239
nmap <F7> :Coveragepy show<CR>

au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/
set encoding=utf-8

"python with virtualenv support
python3 << EOF
import os
import sys
if 'VIRTUAL_ENV' in os.environ:
  project_base_dir = os.environ['VIRTUAL_ENV']
  activate_this = os.path.join(project_base_dir, 'bin/activate_this.py')
  exec(open(activate_this).read(), dict(__file__=activate_this))
EOF

let python_highlight_all=1
syntax on

let NERDTreeIgnore=['\.pyc$', '\~$'] "ignore files in NERDTree
set nu

so ~/.vim/watch_coverage.vim
