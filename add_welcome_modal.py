import re

file_path = r"c:\Users\genna\.gemini\antigravity\scratch\eu-citizenship\index.html"

welcome_modal_html = """
<!-- Welcome Modal -->
<div class="modal-overlay" id="welcomeModal" style="display: none; align-items: center; justify-content: center; position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: rgba(0,0,0,0.85); z-index: 10005; overflow-y: auto;">
<div class="modal-content" style="background: #0B2046; border-radius: 8px; position: relative; max-width: 600px; width: 95%; box-shadow: 0 20px 60px rgba(0,0,0,0.4); margin: auto; padding: 40px; text-align: center;">
    <button onclick="closeWelcomeModal()" onmouseout="this.style.color='rgba(255,255,255,0.5)'" onmouseover="this.style.color='#fff'" style="position: absolute; top: 15px; right: 20px; font-size: 2rem; background: none; border: none; cursor: pointer; color: rgba(255,255,255,0.5); line-height: 1; transition: 0.3s; z-index: 2;">×</button>
    
    <div class="modal-topic-badge" style="display: inline-block; padding: 6px 14px; background: rgba(212,175,55,0.1); color: var(--gold-main); border-radius: 20px; font-size: 0.75rem; font-weight: 600; text-transform: uppercase; margin-bottom: 20px; border: 1px solid rgba(212,175,55,0.2);">Срочная новость</div>
    <h3 style="font-family: 'Times New Roman', serif; font-size: 2rem; color: #FFFFFF; margin-top: 0; margin-bottom: 15px; line-height: 1.2;">Ускоренная процедура<br/>оформления гражданства</h3>
    <p style="color: rgba(255,255,255,0.7); font-size: 1rem; line-height: 1.6; margin-bottom: 25px;">Узнайте, как сократить сроки благодаря новым изменениям в законодательстве. Оставьте номер телефона для бесплатной оценки шансов.</p>
    
    <form action="/telegram.php" method="POST" id="welcome-form" style="display: flex; flex-direction: column; gap: 15px; max-width: 400px; margin: 0 auto;">
        <input type="hidden" name="service_type" value="Ускоренная процедура">
        <input class="dark-modal-input" name="name" placeholder="Ваше имя" required="" type="text" style="width: 100%; padding: 15px 18px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.1); background: rgba(255,255,255,0.03); color: #fff; box-sizing: border-box; outline: none; transition: border-color 0.3s;"/>
        <input class="dark-modal-input" id="welcome-phone" name="phone" placeholder="Номер телефона (например, +7...)" required="" type="tel" style="width: 100%; padding: 15px 18px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.1); background: rgba(255,255,255,0.03); color: #fff; box-sizing: border-box; outline: none; transition: border-color 0.3s;"/>
        <div id="phone-error" style="color: #e53e3e; font-size: 0.85rem; display: none; text-align: left; margin-top: -10px;">Пожалуйста, введите корректный номер (минимум 10 цифр)</div>
        <button onmouseout="this.style.background='#eab308'" onmouseover="this.style.background='#d19e07'" style="width: 100%; padding: 16px; font-size: 1rem; border-radius: 6px; border: none; font-weight: 600; cursor: pointer; background: linear-gradient(90deg, #d4af37, #b8860b); color: #111; transition: 0.3s;" type="submit">Узнать подробнее</button>
        <div style="font-size: 0.75rem; color: rgba(255,255,255,0.4); margin-top: 5px;">Мы гарантируем конфиденциальность.</div>
    </form>
</div>
</div>

<script>
function closeWelcomeModal() {
    var wm = document.getElementById('welcomeModal');
    if(wm) {
        wm.style.display = 'none';
        document.body.style.overflow = 'auto';
        localStorage.setItem('welcome_modal_shown', 'true');
    }
}

document.addEventListener('DOMContentLoaded', function() {
    // Only show if not shown before in localStorage
    if(!localStorage.getItem('welcome_modal_shown')) {
        setTimeout(function() {
            var wm = document.getElementById('welcomeModal');
            if(wm) {
                wm.style.display = 'flex';
                document.body.style.overflow = 'hidden';
            }
        }, 1500); // 1.5 seconds delay
    }

    var form = document.getElementById('welcome-form');
    var phoneInput = document.getElementById('welcome-phone');
    var phoneError = document.getElementById('phone-error');

    if(form) {
        // Handle input focus styling
        var inputs = form.querySelectorAll('.dark-modal-input');
        inputs.forEach(inp => {
            inp.addEventListener('focus', () => inp.style.borderColor = '#d4af37');
            inp.addEventListener('blur', () => {
                if(inp.id !== 'welcome-phone' || phoneError.style.display === 'none') {
                    inp.style.borderColor = 'rgba(255,255,255,0.1)';
                }
            });
        });

        // Form Validation
        form.addEventListener('submit', function(e) {
            var phoneVal = phoneInput.value.replace(/\\D/g, ''); // strip all non-digits
            if(phoneVal.length < 10) {
                e.preventDefault(); // stop submission
                phoneError.style.display = 'block';
                phoneInput.style.borderColor = '#e53e3e';
            } else {
                phoneError.style.display = 'none';
                phoneInput.style.borderColor = 'rgba(255,255,255,0.1)';
                localStorage.setItem('welcome_modal_shown', 'true');
                // Allow submission
            }
        });
    }

    // Close when clicking outside content area
    var wm = document.getElementById('welcomeModal');
    if(wm) {
        wm.addEventListener('click', function(e) {
            if(e.target === wm) closeWelcomeModal();
        });
    }
});
</script>
<!-- End Welcome Modal -->
"""

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if "welcomeModal" not in content:
        content = content.replace('</body>', welcome_modal_html + '\n</body>')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Welcome modal successfully injected!")
    else:
        print("Welcome modal already exists.")
except Exception as e:
    import traceback
    traceback.print_exc()
