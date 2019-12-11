set nocompatible              " be iMproved, required
filetype off 
let mapleader=";" 
let $WORKDIR=$HOME . '/projects'
let $VIMFILES=$HOME . '/.vim'
"let NERDTreeIgnore=['^[A-B].*', '^[D-Z].*', '^Ca.*', '^Co.*', '^CT.*', '\~$']


set rtp+=$VIMFILES/bundle/Vundle.vim
call vundle#begin($VIMFILES.'/bundle/')

Plugin 'git://github.com/VundleVim/Vundle.vim'
Plugin 'git://github.com/tomasr/molokai'
Plugin 'git://github.com/scrooloose/nerdtree'
"Plugin 'jistr/vim-nerdtree-tabs'
Plugin 'git://github.com/scrooloose/syntastic'
Plugin 'git://github.com/scrooloose/nerdcommenter'
Plugin 'git://github.com/kien/ctrlp.vim'
Plugin 'git://github.com/easymotion/vim-easymotion'
Plugin 'git://github.com/szw/vim-tags'
Plugin 'git://github.com/dkprice/vim-easygrep'
Plugin 'git://github.com/skwp/greplace.vim'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
Plugin 'git://github.com/amiorin/vim-project'

Plugin 'git://github.com/godlygeek/tabular'
Plugin 'git://github.com/plasticboy/vim-markdown'
Plugin 'git://github.com/tpope/vim-repeat'
Plugin 'git://github.com/Houl/vim-repmo'
Plugin 'git://github.com/tpope/vim-surround'
"Plugin 'git://github.com/mtscout6/syntastic-local-eslint.vim'

"Plugin 'garbas/vim-snipmate'            " Snippets manager
"Plugin 'MarcWeber/vim-addon-mw-utils'   " dependencies #1
"Plugin 'tomtom/tlib_vim'                " dependencies #2
"Plugin 'honza/vim-snippets'             " snippets repo
 
" --- Python ---
Plugin 'git://github.com/Vimjas/vim-python-pep8-indent'
"Plugin 'git://github.com/klen/python-mode'               " Python mode (docs, refactor, lints, highlighting, run and ipdb and more)
"Plugin 'git://github.com/davidhalter/jedi-vim'           " Jedi-vim autocomplete plugin
"Plugin 'mitsuhiko/vim-jinja'            " Jinja support for vim
"Plugin 'mitsuhiko/vim-python-combined'  " Combined Python 2/3 for Vim

" --- PHP ----
"Plugin 'git://github.com/shawncplus/phpcomplete.vim.git'
"Plugin 'git://github.com/2072/php-indenting-for-vim'
"Plugin 'git://github.com/StanAngeloff/php.vim.git'

"-----Js---
"Plugin 'git://github.com/mxw/vim-jsx'
"Plugin 'git://github.com/elzr/vim-json'
"Plugin 'git://github.com/pangloss/vim-javascript'
"Plugin 'git://github.com/mtscout6/syntastic-local-eslint.vim'

call vundle#end()            " required

call project#rc("~/projects")

Project 'fv'
Project 'adminportal/em'
Project 'adminportal/nap'
Project 'adminportal/portal_libs'
Project 'cp'
Project 'cp3'
Project 'sp_v2'
Project 'am_v3'
Project 'snm'
Project 'autocards'
Project 'em2'
Project 'pp'

Project 'sales_db'
Project 'newportal_db'
Project 'sales_v2_db'
Project 'attackmanager_db'

Project 'clconsole'
Project 'apiserver'
Project 'messagebus-core'
Project 'collector'
Project 'dispatcher'
Project 'proto/ws_proxy'
Project 'proto/faust_em'
Project 'proto/latexpdf'
Project 'proto/htmlpdf'
"Project 'sales_portal'
Project 'del/oldam_v2'
Project 'study'
"Project 'oldsp_v1'
"Project 'solve_cp'

"function! TabTitle()
    "let title = expand("%:p:t")
    "let t:title = exists("b:title") ? strpart(b:title,0,4) . '|' . title  : title
"endfunction
function! TabTitle()
    let title = expand("%:p:t")
    let t:title = title
endfunction

function! SetGuiTabLabel(var) abort
    set guitablabel=%{GuiTabLabel()}
endfunction

function! GuiTabLabel()
    let label = ''
    let bufnrlist = tabpagebuflist(v:lnum)

    " Add '+' if one of the buffers in the tab page is modified
    for bufnr in bufnrlist
        if getbufvar(bufnr, "&modified")
            let label = '+'
            break
        endif
    endfor

    " Append the number of windows in the tab page if more than one
    let wincount = tabpagewinnr(v:lnum, '$')
    if wincount > 1
        let label .= wincount
    endif
    if label != ''
        let label .= ' '
    endif

    " Append the buffer name
    return label . bufname(bufnrlist[tabpagewinnr(v:lnum) - 1])
endfunction


"autocmd TabEnter *.php,*.tpl.*.css,*.js :NERDTree | :winc p | :NERDTreeFind | :winc p


"autocmd BufReadPost *
"			\ if line("'\"") > 1 && line("'\"") <= line("$") |
"			\   exe "normal! g`\"" |
"			\ endif

" close nerdtree tabs and save session on close vim
"autocmd VimLeave * NERDTreeTabsClose
"autocmd VimLeave * if argc() == 0 | mksession! $VIMFILES/last.session | endif
"
autocmd WinLeave * NERDTreeClose

" clear useless spaces
autocmd BufWrite $WORKDIR/* :%s/\s\+$//ge
" before tab too
autocmd BufWrite $WORKDIR/* :%s/\ \+\t/\t/ge

" I don't want the docstring window to popup during completion
"autocmd FileType python setlocal completeopt-=preview

filetype plugin indent on

if has('gui_running')
	syntax on
	set background=dark
	colorscheme molokai
else
	syntax on
	set t_Co=256
	" mc like sheme
	colorscheme molokai
	"dont ask why - just need it on consoles
	"set background=light
	"set background=dark
endif

let NERDTreeWinSize=30
let g:nerdtree_tabs_open_on_gui_startup=0
let g:nerdtree_tabs_open_on_new_tab=0

"let php_folding = 1
"let php_noShortTags = 1
"let php_parent_error_close = 1
"let php_parent_error_open = 1

let g:EasyGrepReplaceWindowMode=2
let g:EasyGrepSearchCurrentBufferDir=0
let g:EasyGrepRecursive=1
let g:EasyGrepIgnoreCase=1
let g:EasyGrepCommand=1
let g:EasyGrepFilesToExclude=".svn,.git,*/tmp/*,*.so,*.swp,*.zip,*pycache*,*node_modules*,*pyvenv*,*build*,*dump*,*.js*,*.css*,*.svg"

let g:ctrlp_working_path_mode='a'
"let g:ctrlp_custom_ignore = '*(node_modeles|pyvenv).*'
set wildignore+=*/tmp/*,*.so,*.swp,*.zip,*pycache*,*/node_modules/*,*/pyvenv/*,*/build/*,*dump*,*.log,*.xml

let NERDTreeIgnore=['\.pyc$', '\~$']

let g:NERDDefaultAlign = 'left'
let g:NERDTreeQuitOnOpen = 3

"let g:pdv_template_dir = $VIMFILES."/bundle/pdv/templates"

let g:airline_theme = 'base16_bright'
"let g:airline_inactive_collapse=1
let g:airline#extensions#whitespace#enabled = 1
let g:airline#extensions#whitespace#mixed_indent_algo = 1
"let g:airline#extensions#tabline#enabled = 1
"let g:airline#extensions#tabline#tab_nr_type = 1
"let g:airline#extensions#tabline#show_buffers = 1
"let g:airline#extensions#tabline#show_tab_type = 0
"let g:airline#extensions#tabline#show_splits = 0
"let g:airline#extensions#tabline#fnamemod = ':t'
"let g:airline#extensions#tabline#keymap_ignored_filetypes = ['vimfiler', 'nerdtree']
"let g:airline#extensions#tabline#show_close_button = 0
"let airline#extensions#tabline#ignore_bufadd_pat =
"            \ '\c\vgundo|undotree|vimfiler|tagbar|nerd_tree'

let g:airline_left_sep=''
let g:airline_right_sep=''

"let g:pymode_python = 'python'
"let g:jsx_ext_required = 0
"let g:jedi#completions_command = "<C-N>"


" Syntactic
let g:syntastic_mode_map = { 'mode': 'active',
                          \ 'active_filetypes': ['python'],
                          \ 'passive_filetypes': ['javascript'] }
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0
let g:syntastic_aggregate_errors = 1
let g:syntastic_loc_list_height = 10

let g:syntastic_error_symbol = '❌'
let g:syntastic_style_error_symbol = '⁉️'
let g:syntastic_warning_symbol = '⚠️'
let g:syntastic_style_warning_symbol = '💩'

highlight link SyntasticErrorSign SignColumn
highlight link SyntasticWarningSign SignColumn
highlight link SyntasticStyleErrorSign SignColumn
highlight link SyntasticStyleWarningSign SignColumn

"let g:syntastic_python_checkers = ['prospector', 'mypy']
let g:syntastic_python_checkers = ['flake8', 'bandit']
let g:syntastic_php_checkers = ['php', 'phpcs']
autocmd FileType php let g:syntastic_php_phpcs_args = '--standard=' . getcwd() . '/.phpstandart.xml'
let g:syntastic_javascript_checkers = ['eslint']
"let g:syntastic_javascript_eslint_exe='$(npm bin)/eslint'
"let g:syntastic_javascript_eslint_exe = 'npm run lint --'
" -Syntactic
"let g:syntastic_ignore_files = ['kdp_attack_manager']


set ff=unix
set ffs=unix,dos
"set ffs=unix,dos
set fileencoding=utf-8
set encoding=utf-8
" Отображение кириллицы во внутренних сообщениях программы
" lan mes ru_RU.UTF-8
" Отображение кириллицы в меню
" source $VIMRUNTIME/delmenu.vim
" set langmenu=ru_RU.UTF-8
" source $VIMRUNTIME/menu.vim

set listchars=tab:.\ ,trail:~
set list
set number
set incsearch
set nohlsearch

set tabstop=2
set shiftwidth=2
set softtabstop=2

autocmd BufRead,BufNewFile *.php setlocal tabstop=4 shiftwidth=4 softtabstop=4
autocmd Filetype python setlocal tabstop=4 shiftwidth=4 softtabstop=4

set colorcolumn=120
autocmd Filetype python setlocal colorcolumn=80
autocmd Filetype php setlocal colorcolumn=100

set smarttab
set smartindent
set expandtab
set showcmd
set mouse=a
set so=10
set noautowrite
set timeout timeoutlen=2000 ttimeoutlen=100

"set sessionoptions=curdir,help,resize,winpos,winsize,tabpages
set guioptions=ia
set gdefault
set ignorecase
set laststatus=2
set guifont=:h13:cRUSSIAN
set guifont=Dejavu\ Sans\ Mono\ 13
set tags+=$VIMFILES/tags.txt
"set langmap=ФИСВУАПРШОЛДЬТЩЗЙКЫЕГМЦЧНЯ;ABCDEFGHIJKLMNOPQRSTUVWXYZ,фисвуапршолдьтщзйкыегмцчня;abcdefghijklmnopqrstuvwxyz

"func! MyFoldText()
  "let count_lines = v:foldend - v:foldstart - 1
  "let line_start = substitute(getline(v:foldstart), '/\*\|\*/\|{{{\d\=', '', 'g')
  "let line_end = substitute(getline(v:foldend), '/\*\|\*/\|{{{\d\=', '', 'g')
  "return v:folddashes . line_start . '  ' . count_lines . " lines   " . line_end
"endfunction
"set foldmethod=manual
"set foldlevel=1
"set fillchars=vert:\|
"set foldtext=MyFoldText()
set nofoldenable

"set foldminlines=0
map <Leader> <Plug>(easymotion-prefix)
nmap <C-]> g<C-]>
nmap <C-p> :CtrlP getcwd()<CR>
nmap <A-f> :tab Grep<Space>
" update CtrlP cache and update ctgs
nmap <Leader>re :CtrlPClearAllCache<CR>:exe ':!ctags -R -f "'.$VIMFILES.'/tags.txt" --exclude="*pyvenv*" --exclude="*.min.js" --exclude="*node_modules*" --exclude="*build*" --exclude="*dist*" -F "'.getcwd().'"'<CR>
nmap <Leader>tf :NERDTreeFind<CR>
"nmap <Leader>to :NERDTreeMirrorToggle<CR>
"nmap <Leader>tc :NERDTreeClose<CR>
nmap <Leader>z :1,1000bw<CR>
map <Leader>y "+y
map <Leader>p "+p
map <A-l> :tabn<CR>
map <A-h> :tabp<CR>
map <Leader>H :tabmove -1<CR>
map <Leader>L :tabmove +1<CR>
"map <Leader>h <C-w>h:vertical res 120<CR> 
"map <Leader>l <C-w>l:vertical res 120<CR>
nmap <leader>1 :tabn 1<CR>
nmap <leader>2 :tabn 2<CR>
nmap <leader>3 :tabn 3<CR>
nmap <leader>4 :tabn 4<CR>
nmap <leader>5 :tabn 5<CR>
nmap <leader>6 :tabn 6<CR>
nmap <leader>7 :tabn 7<CR>
nmap <leader>8 :tabn 8<CR>
nmap <leader>9 :tabn 9<CR>
nmap <leader>qa :%s/\s\+$//ge<CR>:%s/\ \+\t/\t/ge<CR>
nmap <leader>s :vertical res 120<CR>
nmap <leader>n :lnext<CR>
nmap <leader>N :lprevious<CR>
nmap <leader>m :ll<CR>

nmap <leader><leader>w :tabnew<CR>:Welcome<CR>
nmap <leader><leader>W :tabnew<CR>:Welcome<CR>

nmap <leader>ts :SyntasticToggleMode<CR>
nmap <leader>c :SyntasticCheck<CR>
nmap <F2> :SyntasticCheck<CR>

" enclose word in commas
"nmap <Plug>DoubleQuaters2 ciw"" <Esc>P
"nnoremap <silent> <Plug>DoubleQuaters ciw"" :call repeat#set("\<Plug>DoubleQuaters")<CR>
"nmap <silent> <Plug>SingleQuaters ciw''<Esc>P :call repeat#set("\<Plug>SingleQuaters")<CR>

"nnoremap <Leader>q" <Plug>DoubleQuaters2
"nnoremap <Leader>q' <Plug>SingleQuaters
"nnoremap <Leader>qd daW"=substitute(@@,"'\\\|\"","","g")<CR>P



"command C write | !hg commit -m 'quick commit' && hg push
command W write

abclear
iabbrev /** /**<CR><CR>/<UP>
iabbrev pdb import pdb; pdb.set_trace()
iabbrev p_r print '<pre>' . print_r(, true) . '</pre>'; exit;

