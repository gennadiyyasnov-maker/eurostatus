with open('assets/js/main.js', 'a', encoding='utf-8') as f:
    f.write("""

// Telegram Form Forwarder
document.addEventListener('DOMContentLoaded', () => {
    const forms = document.querySelectorAll('form[action="#"], form.lead-form');
    
    forms.forEach(form => {
        // Only attach if it's not the crisp text area form that has name="form_message"
        if(form.getAttribute('name') === 'form_message') return;

        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const submitBtn = form.querySelector('button[type="submit"]');
            const originalBtnText = submitBtn ? submitBtn.innerText : 'Отправить';
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerText = 'Отправка...';
            }

            const formData = new FormData(form);
            
            try {
                const response = await fetch('/telegram.php', {
                    method: 'POST',
                    body: formData
                });
                
                const result = await response.json();
                
                if (result.status === 'success') {
                    if (submitBtn) {
                        submitBtn.innerText = 'Заявка отправлена!';
                        submitBtn.style.backgroundColor = '#2ecc71';
                        submitBtn.style.color = '#fff';
                        submitBtn.style.borderColor = '#2ecc71';
                    }
                    form.reset();
                    // Reset custom select if exists
                    const customSelectText = form.querySelector('.custom-select-trigger span');
                    if (customSelectText) {
                        customSelectText.innerText = 'Услуга выбрана';
                    }
                    setTimeout(() => {
                        if (submitBtn) {
                            submitBtn.disabled = false;
                            submitBtn.innerText = originalBtnText;
                            submitBtn.style = ''; // reset inline styles
                        }
                    }, 5000);
                } else {
                    alert('Ошибка: ' + (result.message || 'Не удалось отправить заявку.'));
                    if (submitBtn) {
                        submitBtn.disabled = false;
                        submitBtn.innerText = originalBtnText;
                    }
                }
            } catch (err) {
                console.error(err);
                alert('Произошла ошибка при отправке. Пожалуйста, попробуйте позже.');
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.innerText = originalBtnText;
                }
            }
        });
    });
});
""")
