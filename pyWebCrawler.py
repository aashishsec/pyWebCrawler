import requests,argparse,re,random,colorama,concurrent.futures

from bs4 import BeautifulSoup

from datetime import datetime

from urllib.parse import urljoin

from colorama import Fore, Style

colorama.init(autoreset=True)

green = Fore.GREEN

magenta = Fore.MAGENTA

cyan = Fore.CYAN

mixed = Fore.RED + Fore.BLUE

red = Fore.RED

blue = Fore.BLUE

yellow = Fore.YELLOW

white = Fore.WHITE

reset = Style.RESET_ALL

colors = [magenta,cyan,mixed,red,blue,yellow, white]

random_color = random.choice(colors)

bold = Style.BRIGHT

global_output=[]

class WebCrawler:

    global global_output

    def __init__(self, url, max_depth,threads,output):

        self.url = url

        self.max_depth = max_depth

        self.threads=threads

        self.output=output

        self.subdomains = set()

        self.links = set()
        
        self.jsfiles = set()

    def start_crawling(self):

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.threads) as executor:
            
            executor.submit(self.crawl, self.url, depth=1)


    def crawl(self, url, depth):

        if depth > self.max_depth:

            return

        try:

            response = requests.get(url, timeout=3, allow_redirects=True)

            soup = BeautifulSoup(response.text, 'html.parser')

        except requests.exceptions.RequestException as err:

            print(f"[-] An error occurred: {err}")

            return

        subdomain_query = fr"https?://([a-zA-Z0-9.-]+)"

        for link in soup.find_all('a'):

            link_text = link.get('href')

            if link_text:

                if re.match(subdomain_query, link_text) and link_text not in self.subdomains:

                    self.subdomains.add(link_text)

                else:

                    full_link = urljoin(url, link_text)

                    if full_link != url and full_link not in self.links:

                        self.links.add(full_link)

                        self.crawl(full_link, depth + 1)

        for file in soup.find_all('script'):

            script_src = file.get('src')

            if script_src:

                self.jsfiles.add(script_src)

    def print_banner(self):

        print(f'''{bold}{random_color}

██████╗░██╗░░░██╗░█████╗░██████╗░░█████╗░░██╗░░░░░░░██╗██╗░░░░░███████╗██████╗░
██╔══██╗╚██╗░██╔╝██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║██║░░░░░██╔════╝██╔══██╗
██████╔╝░╚████╔╝░██║░░╚═╝██████╔╝███████║░╚██╗████╗██╔╝██║░░░░░█████╗░░██████╔╝
██╔═══╝░░░╚██╔╝░░██║░░██╗██╔══██╗██╔══██║░░████╔═████║░██║░░░░░██╔══╝░░██╔══██╗
██║░░░░░░░░██║░░░╚█████╔╝██║░░██║██║░░██║░░╚██╔╝░╚██╔╝░███████╗███████╗██║░░██║
╚═╝░░░░░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝╚═╝░░╚═╝
              
               Author   : Aashish💕💕  
                                              
               Github   : https://github.com/aashishsec
              
               pyCrawler is a tool designed to automatically extracting urls and Js from websites.

        ''')

        print("-" * 80)

        print(f"{bold}{random_color}Recursive PyCrawler starting at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

        print("-" * 80)

        print(f"{bold}{random_color}[*] URL".ljust(20, " "), ":", self.url)

        print(f"{bold}{random_color}[*] Max Depth".ljust(20, " "), ":", self.max_depth)

        print(f"{bold}{random_color}[*] Threads".ljust(20, " "), ":", self.threads)

        print("-" * 80)

    def print_results(self):

        if self.subdomains:

            for subdomain in self.subdomains:

                print(f"{bold}{random_color}[+] Subdomains : {subdomain}")

                global_output.append(f"[+] Subdomains : {subdomain}")

        print()

        if self.links:

            for link in self.links:

                print(f"{bold}{random_color}[+] Links : {link}")

                global_output.append(f"[+] Links : {link}")

        print()

        if self.jsfiles:

            for file in self.jsfiles:

                print(f"{bold}{random_color}[+] JS Files : {file}")

                global_output.append(f"[+] JS Files : {file}")

    def save_output(self):
            
        with open(self.output, 'w') as file:

            file.write('\n'.join(global_output))



def get_args():

    parser=argparse.ArgumentParser(description=f"{bold}{random_color}pyCrawler is a tool designed to automatically extracting Urls, Subdomins and JS Files from websites.")

    parser.add_argument('-u', '--url', dest='url', help=f"{bold}{random_color}Specify the URL, provide it along http/https", required=True)

    parser.add_argument('-d', '--depth', dest='depth', type=int, default=1, help=f"{bold}{random_color}Specify the recursion depth limit.")

    parser.add_argument('-t', '--threads', dest='threads', type=int, default=100, help=f"{bold}{random_color}Specify the threads, default=100.")

    parser.add_argument('-o', '--output', dest='output', default="pyWebCrawler.txt", help=f"{bold}{random_color}Specify the file u want to save, default=pyWebCrawler.txt")

    return parser.parse_args()



if __name__ == "__main__":

    args = get_args()

    web_crawler = WebCrawler(args.url, args.depth,args.threads,args.output)

    web_crawler.print_banner()

    web_crawler.start_crawling()

    web_crawler.print_results()

    web_crawler.save_output()
