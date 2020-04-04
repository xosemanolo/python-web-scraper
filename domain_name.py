from tld import get_fld

def get_domain_name(url):

    domain_name = get_fld(url)
    return domain_name

print('1')
print(get_domain_name('https://www.facebook.com/'))
print('3')