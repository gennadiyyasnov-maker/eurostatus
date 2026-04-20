import os

file_path = 'assets/js/lang.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# I am replacing the entirety of the cookie handling logic natively
new_cookie_logic = """
/* --- Cookie Handling --- */
// Function to get cookie value by name
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
    return null;
}

function setTranslateCookie(lang) {
    document.cookie = `googtrans=/ru/${lang}; path=/;`;
    document.cookie = `googtrans=/ru/${lang}; path=/; domain=.${location.hostname}`;
}

function clearAllGoogtransCookies() {
    // Aggressively delete the googtrans cookie from all possible domain scopes
    const domainParts = location.hostname.split('.');
    document.cookie = "googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    
    // Iterate backwards through domains to wipe .twc1.net, .domain.net, etc
    for (let i = 0; i < domainParts.length; i++) {
        const domainStr = domainParts.slice(i).join('.');
        document.cookie = `googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; domain=${domainStr}; path=/;`;
        document.cookie = `googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; domain=.${domainStr}; path=/;`;
    }
}
"""

content = content.replace(
"""/* --- Cookie Handling --- */
// Function to get cookie value by name
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
    return null;
}

function setTranslateCookie(lang) {
    document.cookie = `googtrans=/ru/${lang}; path=/;`;
    document.cookie = `googtrans=/ru/${lang}; path=/; domain=.${location.hostname}`;
}""", new_cookie_logic)


# Now fix the click listener natively
new_click_listener = """
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const text = link.textContent.trim().toLowerCase();
            
            if (text === 'en' && currentLang !== 'en') {
                setTranslateCookie('en');
                window.location.reload();
            } else if (text === 'ru' && currentLang !== 'ru') {
                clearAllGoogtransCookies();
                // We also set the url parameter without reload then reload hard
                window.location.reload();
            }
        });
"""

# Find the old listener code
import re
content = re.sub(r"link\.addEventListener\('click', \(e\) => \{[\s\S]*?window\.location\.reload\(\);\n\s*\}\);\n\s*\}\);", 
"""        link.addEventListener('click', (e) => {
            e.preventDefault();
            const text = link.textContent.trim().toLowerCase();
            
            if (text === 'en' && currentLang !== 'en') {
                setTranslateCookie('en');
                window.location.reload();
            } else if (text === 'ru' && currentLang !== 'ru') {
                clearAllGoogtransCookies();
                // A double whammy: also clear any local storage that might persist translations
                localStorage.removeItem('googtrans');
                sessionStorage.removeItem('googtrans');
                window.location.reload();
            }
        });
    });""", content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
