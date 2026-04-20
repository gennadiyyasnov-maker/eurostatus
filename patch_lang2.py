import os, re

file_path = 'assets/js/lang.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Make cookie wiping super resilient
new_cookie = """function setTranslateCookie(lang) {
    document.cookie = `googtrans=/ru/${lang}; path=/;`;
    if (lang === 'en') {
        document.cookie = `googtrans=/ru/${lang}; path=/; domain=.${location.hostname}`;
    }
}

function obliterateTranslateCookies() {
    // Aggressively delete ALL cookies matching googtrans
    const domains = [
        location.hostname,
        `.${location.hostname}`,
        location.hostname.split('.').slice(1).join('.'), // usually the main domain
        `.${location.hostname.split('.').slice(1).join('.')}`
    ];
    
    // Explicitly target root path and common variations
    domains.forEach(d => {
        document.cookie = `googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/; domain=${d}`;
        document.cookie = `googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;`;
    });
    
    // Also clear from local storage
    try {
        localStorage.removeItem('googtrans');
        sessionStorage.removeItem('googtrans');
    } catch(e){}
}
"""

content = re.sub(r'function setTranslateCookie\(lang\) \{[\s\S]*?\}', new_cookie, content, count=1)

# Modify click event
new_click = """    document.body.addEventListener('click', (e) => {
        const langLink = e.target.closest('.lang-switch a');
        if (langLink) {
            e.preventDefault();
            const text = langLink.textContent.trim().toLowerCase();
            
            if (text === 'en' && currentLang !== 'en') {
                setTranslateCookie('en');
                window.location.reload();
            } else if (text === 'ru' && currentLang !== 'ru') {
                obliterateTranslateCookies();
                window.location.reload();
            }
        }
    });"""

content = re.sub(r"document\.body\.addEventListener\('click', \(e\) => \{[\s\S]*?\}\);\n    \}\);", new_click, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
