import requests , os , platform , re , time
from ping3 import verbose_ping
from bs4 import BeautifulSoup
from rich.console import Console
console = Console()

username = os.environ.get("USERNAME")
platformname = platform.system()

teminal_input = f'[{platform.uname()}]-[{os.getlogin()}]'
banner = '''   _____   ___________________    ____ ___  _________   _____    
  /     \  \_   _____/\______ \  |    |   \/   _____/  /  _  \   
 /  \ /  \  |    __)_  |    |  \ |    |   /\_____  \  /  /_\  \  
/    Y    \ |        \ |    `   \|    |  / /        \/    |    \ 
\____|__  //_______  //_______  /|______/ /_______  /\____|__  / 
        \/         \/         \/                  \/         \/  '''
binary_banner = '01001101 01000101 01000100 01010101 01010011 01000001'
combine_banners = f'''
[#8861fa]{banner}[/]
     [#d098fa]{binary_banner}[/]
    
        [#8861fa]]----------[[#d098fa]+[/]][/] Coded By Mahyar [#8861fa][[#d098fa]+[/]]----------[[/]
    [#8861fa]]-----[[#d098fa]+[/]][/] https://github.com/Mhyar-nsi/Medusa [#8861fa][[#d098fa]+[/]]-----[[/]
''' 
tools_list = '''
     [#1B769C][[/][#67bde0]1[/][#1B769C]][/] Wordpress Scan          [#1B769C][[/][#67bde0]2[/][#1B769C]][/] Wordpress Admin panel 
     [#d19d19][[/][#edd79f]3[/][#d19d19]][/] Read robots.txt         [#d19d19][[/][#edd79f]4[/][#d19d19]][/] Find Site Map
     [#074391][[/][#6b9ad6]5[/][#074391]][/] Website ping            [#074391][[/][#6b9ad6]6[/][#074391]][/] Domain to IP
     [#09ba68][[/][#82e8b8]7[/][#09ba68]][/] DNS lookup              [#09ba68][[/][#82e8b8]8[/][#09ba68]][/] Website ping
     [#09ba68][[/][#82e8b8]9[/][#09ba68]][/] Find file by format

                       [#b30024][[/][#fc6583]99[/][#b30024]][/] Exit 
'''
  
def clear_screen():
    OS = platform.system()
    if OS == 'Windows':
        os.system('cls')
    elif OS == 'Linux' or OS == 'Darwin':
        os.system('clear') 
        
def timer():      
    print('')
    tasks = [f"task {n}" for n in range(0, 1)]
    with console.status("[bold blue]It will be deleted in 5 seconds.") as status:
        while tasks:
            task = tasks.pop(0)
            time.sleep(5)
    clear_screen()
            
def request(url):
    print('Plase Wait...')
    try:
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0'}
        response = requests.get(url , headers=header)
        status_code = response.status_code
        if status_code == 200:
            return {
                'condition' : True,
                'content' : response.content,
                'text' : response.text,
                'status' : status_code
                }
        else:
            return {
                'condition' : False,
                'status' : status_code
            }
    except:
        return {
            'condition' : False,
            'status' : '-',
            'message' : 'url is wrong.'
        }
    
def wp_scan():
    clear_screen()
    print('send target url (example.com) : ')
    url = console.input(f'~> ')
    clear_screen()
    
    if url[0:4] != 'http':
        url = f'https://{url}'
       
    details = request(url) 
    clear_screen()
    if details['condition']:
        console.print(f'[#00ab7a][[/]  [#89fada]ok[/]  [#00ab7a]][/] Your target is : {url}')
        print('')
        time.sleep(2)
        text = details['text']
        isExist = re.search("wp-content", text)
        if isExist:
            console.print('[#00b50f][[/]  [#89fa93]✓[/]   [#00b50f]][/] This website uses WordPress.')
            html = BeautifulSoup(details['content'] , 'html.parser')
            generator_tag = html.findAll('meta' , {'name' : 'generator'})
            len_generator = len(generator_tag)
            if len_generator != 0:
                print('')
                console.print('[#00ab7a][[/]  [#89fada]ok[/]  [#00ab7a]][/] More information ⇣')
                for i in range(0 , len_generator):
                    time.sleep(1)
                    console.print(f'[#00b50f][[/]  [#89fa93]✓[/]   [#00b50f]][/] {generator_tag[i].get("content")}')
        else:
            console.print('[#b30024][[/]  [#fc6583]✘[/]   [#b30024]][/] This website does not use WordPress.')
    else:
        console.print(f'[#b30024][[/]  [#fc6583]![/]   [#b30024]][/] Error {details["status"]}') 
    enter()
  
def check_ping():
    clear_screen()
    url = console.input('[[blue]-[/]] Enter URL [bold blue](example.com)[/] : ')
    
    if url[0:8] == 'https://':
        url = url.replace('https://', '')
    elif url[0:7] == 'http://':
        url = url.replace('http://', '')
        
    cou = console.input('[[blue]-[/]] Enter the number of pings [bold blue](default 10)[/] : ') or 10
    inter = console.input('[[blue]-[/]] Enter the interval between each ping [Second] [bold blue](default 3)[/] : ') or 3
    print('')
    verbose_ping(url , count=int(cou) , interval=int(inter))

    timer()
    run()
 
def read_robots():
    clear_screen()
    print('send target url (example.com) : ')
    url = console.input(f'~> ')
    clear_screen()
    if url[0:4] != 'http':
        url = f'https://{url}' 
    details = request(f'{url}/robots.txt')
    clear_screen()
    if details['condition']:
        print(details['text'])
        robots_file = details['text']
        console.print(f'Do wan\'t save {url[8:]} robots.txt ? (Y/n)')
        save = console.input('~> ').lower()
        if save == 'y':
            isDir = os.path.isdir(url[8:])
            if isDir == False:
                os.mkdir(url[8:])
            with open(f'./{url[8:]}/robots.txt' , 'a') as file:
                file.write(robots_file)   
    enter()
    
def enter():
    print('')
    console.input("Press [#568dd6 underline]Enter[/] to continue[#ffffff]...[/]")
    run()
    
def run():
    clear_screen()
    console.print(combine_banners)
    console.print(tools_list)
    selected = int(console.input(f'''[#8861fa]┌──([/][#d098fa]{platformname.lower()}@{username}[/][#8861fa])-[[/][#d098fa]~/medusa[/][#8861fa]][/]
[#8861fa]└$[/] '''))
    
    if selected == 1:
        wp_scan()
    elif selected == 9:
        check_ping()
    elif selected == 3:
        read_robots()
    elif selected == 99:
        clear_screen()
        exit()
    
if __name__ == '__main__':
    run()