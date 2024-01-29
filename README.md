# pyWebCrawler
[Tool Link](https://github.com/aashishsec/pyWebCrawler/)

---

![GitHub last commit](https://img.shields.io/github/last-commit/aashishsec/pyWebCrawler) ![GitHub release (latest by date)](https://img.shields.io/github/v/release/aashishsec/pyWebCrawler) [![GitHub license](https://img.shields.io/github/license/aashishsec/pyWebCrawler)](https://github.com/aashishsec/pyWebCrawler/blob/main/LICENSE) [![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/aashishsec/)

- pyCrawler is a Python-based web crawling tool designed to automatically extract URLs, subdomains, and JavaScript files from websites.
  
-  It provides a simple command-line interface for users to specify the target URL, recursion depth, number of threads, and output file.

## Features

- Extracts subdomains, links, and JavaScript files recursively.
  
- Supports multithreaded crawling for improved performance.
  
- Allows customization of recursion depth.
  
- Provides an option to save the output to a specified file.

## Installation

- Clone the repository to your local machine.
  
- Install the required dependencies using pip


```bash
git clone https://github.com/aashish36/pyWebCrawler.git

cd pyWebCrawler

pip install -r requirements.txt

```

## Usage

- Give url to tool that you want to crawl.

- This python code will save the results of the analysis to a file named 'pyWebCrawler.txt'.

- Run the script using the following commands: 

``` bash

usage: webcrawlerMark-2.py [-h] -u URL [-d DEPTH] [-t THREADS] [-o OUTPUT]

pyCrawler is a tool designed to automatically extracting Urls, Subdomins and JS Files from websites.

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     Specify the URL, provide it along http/https
  -d DEPTH, --depth DEPTH
                        Specify the recursion depth limit.
  -t THREADS, --threads THREADS
                        Specify the threads, default=100.
  -o OUTPUT, --output OUTPUT
                        Specify the file u want to save, default=pyWebCrawler.txt

```
## Tool Output

![image](https://github.com/aashishsec/pyWebCrawler/assets/65489287/71897d24-e2ab-4217-b38b-b49c42d678cf)

## Total Tool Output

```bash

██████╗░██╗░░░██╗░█████╗░██████╗░░█████╗░░██╗░░░░░░░██╗██╗░░░░░███████╗██████╗░
██╔══██╗╚██╗░██╔╝██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║██║░░░░░██╔════╝██╔══██╗
██████╔╝░╚████╔╝░██║░░╚═╝██████╔╝███████║░╚██╗████╗██╔╝██║░░░░░█████╗░░██████╔╝
██╔═══╝░░░╚██╔╝░░██║░░██╗██╔══██╗██╔══██║░░████╔═████║░██║░░░░░██╔══╝░░██╔══██╗
██║░░░░░░░░██║░░░╚█████╔╝██║░░██║██║░░██║░░╚██╔╝░╚██╔╝░███████╗███████╗██║░░██║
╚═╝░░░░░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝╚═╝░░╚═╝

               Author   : Aashish💕💕  

               Github   : https://github.com/aashish36

               pyCrawler is a tool designed to automatically extracting urls and Js from websites.

        
--------------------------------------------------------------------------------
Recursive PyCrawler starting at 30/11/2023 07:30:54
--------------------------------------------------------------------------------
[*] URL     : https://hackerone.com
[*] Max Depth : 1
[*] Threads : 100
--------------------------------------------------------------------------------
[+] Subdomains : https://www.hackerone.com/hacktivitycon
[+] Subdomains : https://hackerone.com/security?type=team
[+] Subdomains : https://www.hackerone.com/reports/6th-annual-hacker-powered-security-report
[+] Subdomains : https://www.hackerone.com/customer-hub/Hyatt
[+] Subdomains : https://hackerone.com/hacktivity
[+] Subdomains : https://www.hackerone.com/events
[+] Subdomains : https://www.hackerone.com/product/challenge
[+] Subdomains : https://www.hackerone.com/product/bug-bounty-platform
[+] Subdomains : https://www.hackerone.com/resources
[+] Subdomains : https://www.hackerone.com/partners/integrations
[+] Subdomains : https://hackerone.com/users/sign_in
[+] Subdomains : https://www.philvenables.com/post/bug-bounty-programs
[+] Subdomains : https://www.hackerone.com/product/overview
[+] Subdomains : https://docs.hackerone.com/
[+] Subdomains : https://www.twitter.com/Hacker0x01
[+] Subdomains : https://www.hackerone.com/hackers/hacker101
[+] Subdomains : https://www.hackerone.com/vulnerability-and-security-testing-blog
[+] Subdomains : https://www.hackerone.com/public-policy
[+] Subdomains : https://www.instagram.com/hacker0x01
[+] Subdomains : https://www.linkedin.com/company/hackerone
[+] Subdomains : https://www.hackerone.com/resources/customer-story/zebra-technologies-case-study
[+] Subdomains : https://www.hackerone.com/solutions/vulnerability-management-system
[+] Subdomains : https://www.hackerone.com/leadership
[+] Subdomains : https://hackerone.com/directory/programs?order_direction=DESC&order_field=resolved_report_count
[+] Subdomains : https://www.hackerone.com/customer-stories
[+] Subdomains : https://hackerone.com/leaderboard
[+] Subdomains : https://www.hackerone.com/product/attack-surface-management
[+] Subdomains : https://www.hackerone.com/ebooks/pentesting-matrix
[+] Subdomains : https://hackerone.com/leaderboard/all-time
[+] Subdomains : https://www.hackerone.com/reports/7th-annual-hacker-powered-security-report
[+] Subdomains : https://www.facebook.com/Hacker0x01
[+] Subdomains : https://hackerone.com/opportunities/all/search
[+] Subdomains : https://h1.community/events/#/list

[+] Links : https://hackerone.com/vulnerability-management/zoom-salesforce-ethical-hackers
[+] Links : https://hackerone.com/product/bug-bounty-platform
[+] Links : https://www.hackerone.com/hacktivitycon
[+] Links : https://hackerone.com/partners/integrations
[+] Links : https://hackerone.com/product/attack-surface-management
[+] Links : https://www.hackerone.com/resources
[+] Links : https://www.hackerone.com/partners/integrations
[+] Links : https://hackerone.com/trust
[+] Links : https://hackerone.com/culture-and-talent
[+] Links : https://hackerone.com/thought-leadership/generative-ai-security-predictions
[+] Links : https://www.hackerone.com/vulnerability-and-security-testing-blog
[+] Links : https://hackerone.com/services
[+] Links : https://www.hackerone.com/resources/customer-story/zebra-technologies-case-study
[+] Links : https://hackerone.com/
[+] Links : https://hackerone.com/three-stages-continuous-vulnerability-testing
[+] Links : https://hackerone.com/customer-hub/Nintendo
[+] Links : https://hackerone.com/product/code-security-audit
[+] Links : https://hackerone.com/from-the-ceo
[+] Links : https://hackerone.com/leadership
[+] Links : https://hackerone.com/knowledge-center/devsecops-quick-guide-process-tools-and-best-practices
[+] Links : https://hackerone.com/solutions/vulnerability-management-system
[+] Links : https://hackerone.com/knowledge-center/attack-surface-and-how-analyze-manage-and-reduce-it
[+] Links : https://hackerone.com/vulnerability-management/owasp-llm-vulnerabilities
[+] Links : https://hackerone.com/customer-hub/ATT
[+] Links : https://hackerone.com/solutions/attack-resistance-management
[+] Links : https://hackerone.com/company-news
[+] Links : https://hackerone.com/product/response-vulnerability-disclosure-program
[+] Links : https://hackerone.com/hacktivity
[+] Links : https://hackerone.com#main-content
[+] Links : https://hackerone.com/customer-stories
[+] Links : https://hackerone.com/knowledge-center/principles-threats-and-solutions
[+] Links : https://www.hackerone.com/hackers/hacker101
[+] Links : https://hackerone.com/security-compliance/new-sec-cybersercurity-rules
[+] Links : https://hackerone.com/press
[+] Links : https://hackerone.com/careers
[+] Links : https://hackerone.com/partners/aws
[+] Links : https://hackerone.com/knowledge-center/what-hacking-black-hat-white-hat-blue-hat-and-more
[+] Links : https://hackerone.com/knowledge-center/what-application-security-concepts-tools-best-practices
[+] Links : https://www.hackerone.com/leadership
[+] Links : https://hackerone.com/security-incident
[+] Links : https://hackerone.com/solutions/government
[+] Links : https://hackerone.com/press-archive
[+] Links : https://hackerone.com/vulnerability-and-security-testing-blog
[+] Links : https://hackerone.com/customer-hub/GM
[+] Links : https://hackerone.com/services-2
[+] Links : https://hackerone.com/customer-hub/Hyatt
[+] Links : https://h1.community/events/#/list
[+] Links : https://hackerone.com/knowledge-center/security-compliance-ten-regulations-and-four-tips-success
[+] Links : https://hackerone.com/knowledge-center/what-penetration-testing-how-does-it-work-step-step
[+] Links : https://hackerone.com/hackerone-go
[+] Links : https://hackerone.com/product/challenge
[+] Links : https://hackerone.com/terms
[+] Links : https://hackerone.com/solutions/financial-services
[+] Links : https://hackerone.com/hackerone-community-blog
[+] Links : https://hackerone.com/partners
[+] Links : https://www.hackerone.com/solutions/vulnerability-management-system
[+] Links : https://hackerone.com/knowledge-center/cloud-security-challenges-solutions-and-best-practices
[+] Links : https://hackerone.com/solutions/united-states-federal
[+] Links : https://hackerone.com/contact
[+] Links : https://hackerone.com/leaderboard
[+] Links : https://hackerone.com/product/pentest
[+] Links : https://hackerone.com/solutions/high-growth-companies
[+] Links : https://hackerone.com/solutions/application-security-testing-software
[+] Links : https://hackerone.com/events
[+] Links : https://hackerone.com/knowledge-center/16-types-cybersecurity-attacks-and-how-prevent-them
[+] Links : https://hackerone.com/opportunities/all/search
[+] Links : https://hackerone.com/product/overview
[+] Links : https://hackerone.com/solutions/continuous-security-testing
[+] Links : https://hackerone.com/customer-hub/Paypal
[+] Links : https://www.hackerone.com/events
[+] Links : https://hackerone.com/users/sign_in
[+] Links : https://hackerone.com/knowledge-center/beyond-owasp-top-ten-13-resources-boost-your-security
[+] Links : https://hackerone.com/solutions/cloud-security-solution
[+] Links : https://www.hackerone.com/public-policy
[+] Links : https://hackerone.com/security-compliance/nist-vdp-control
[+] Links : https://hackerone.com/product/insights
[+] Links : https://hackerone.com/knowledge-center/common-vulnerabilities-exposures-glossary-cve
[+] Links : https://hackerone.com/policies
[+] Links : https://hackerone.com/knowledge-center
[+] Links : https://hackerone.com/company
[+] Links : https://hackerone.com/hackers
[+] Links : https://hackerone.com/knowledge-center/website-testing-importance-techniques-5-tips-success
[+] Links : https://hackerone.com/privacy
[+] Links : https://hackerone.com/vulnerability-management/security-advisory-services-sdlc
[+] Links : https://hackerone.com/solutions/united-states-federal-old

[+] JS Files : /sites/default/files/js/js_EOrKavGmjAkpIaCW_cpGJ240OpVZev_5NI-WGIx5URg.js
[+] JS Files : https://cdn.optimizely.com/js/21892691969.js
[+] JS Files : /sites/default/files/google_tag/google_tag/google_tag.script.js?s3z4tf
[+] JS Files : https://consent.trustarc.com/notice?domain=hackerone.com&c=teconsent&js=nj&noticeType=bb&gtm=1
[+] JS Files : ////app-sj17.marketo.com/js/forms2/js/forms2.min.js
```

## Contributing

- Contributions are welcome!
  
- If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

![image](https://github.com/aashish36/JSScanner/assets/65489287/70f7e3a8-e95f-429b-9433-89087daad721)

