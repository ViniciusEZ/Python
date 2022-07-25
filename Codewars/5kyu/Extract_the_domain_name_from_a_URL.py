#Write a function that when given a URL as a string,
# parses out just the domain name and returns it as a string.

def domain_name(url):
    import re
    pattern = re.findall(r'(https?://|www\.)?(www\.)?([a-z0-9-]+)(\..+)?', url)
    return pattern[0][2]


print(domain_name("www.xakep.ru" ))
