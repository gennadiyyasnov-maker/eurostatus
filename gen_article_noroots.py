import os

# HTML template matching the other articles
html_content = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>У меня нет корней: мифы и реальность архивного поиска | EuroStatus</title>
    <meta name="description" content="Узнайте, почему отсутствие информации о корнях не является преградой для получения гражданства ЕС. Как работают архивные юристы и почему 90% граждан СНГ имеют законные основания.">
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="./assets/css/style.css">
    
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "У меня нет корней: как работает архивный поиск",
      "image": "https://eurostatus.online/assets/images/article_no_roots.png",
      "datePublished": "2026-05-14T08:00:00+08:00",
      "dateModified": "2026-05-14T08:00:00+08:00",
      "author": {
        "@type": "Organization",
        "name": "EuroStatus Legal"
      },
      "publisher": {
        "@type": "Organization",
        "name": "EuroStatus",
        "logo": {
          "@type": "ImageObject",
          "url": "https://eurostatus.online/assets/images/logo_light.png"
        }
      },
      "description": "Как восстановить утраченные актовые записи и получить легальное право на гражданство стран Евросоюза, если вы ничего не знаете о своих предках."
    }
    </script>
</head>
<body>
    <!-- HEADER_PLACEHOLDER -->

    <main class="article-page" style="background-color: #f8fafc; padding-bottom: 80px;">
        <div class="container" style="max-width: 900px; margin: 0 auto; padding-top: 40px;">
            
            <a href="/blog" style="display: inline-flex; align-items: center; color: #64748b; text-decoration: none; font-weight: 500; margin-bottom: 30px; transition: color 0.3s;">
                <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 8px;"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
                Вернуться ко всем статьям
            </a>

            <article style="background: white; border-radius: 20px; overflow: hidden; box-shadow: 0 20px 40px rgba(11,32,70,0.05);">
                <div class="article-hero" style="position: relative; height: 450px;">
                    <img src="./assets/images/article_no_roots.png" alt="Восстановление архивных документов" style="width: 100%; height: 100%; object-fit: cover;">
                    <div style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(11,32,70,0.9), transparent);"></div>
                    <div style="position: absolute; bottom: 0; left: 0; padding: 40px;">
                        <span style="background: #CCA352; color: white; padding: 6px 14px; border-radius: 30px; font-size: 0.85rem; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 15px; display: inline-block;">Экспертиза</span>
                        <h1 style="color: white; font-size: 2.8rem; font-family: 'Playfair Display', serif; line-height: 1.2; margin: 0;">«У меня нет корней»: Главный миф об иммиграции и как работают архивы</h1>
                    </div>
                </div>

                <div class="article-content" style="padding: 50px; font-size: 1.15rem; line-height: 1.8; color: #334155;">
                    <p class="lead" style="font-size: 1.3rem; font-weight: 500; color: #0B2046; margin-bottom: 30px; border-left: 4px solid #CCA352; padding-left: 20px;">
                        Это самое частое возражение, которое мы слышим на консультациях. 90% граждан СНГ искренне убеждены, что если их бабушка родилась в Сибири или на Урале, то путь в Евросоюз через репатриацию для них навсегда закрыт. И это глубочайшее заблуждение.
                    </p>

                    <h2 style="color: #0B2046; font-family: 'Playfair Display', serif; font-size: 2rem; margin: 40px 0 20px;">Исторический контекст: куда исчезли данные?</h2>
                    <p>
                        Чтобы понять, почему отсутствие семейных преданий о европейских предках не является приговором, нужно посмотреть на историю ХХ века. Границы государств Восточной Европы и СССР, в частности Бессарабии, Северной Буковины и Одесской области, перекраивались несколько раз.
                    </p>
                    <p>
                        Только во время Великой Отечественной войны и сталинских репрессий миллионы людей подверглись принудительной эвакуации, депортации и ссылкам. Люди меняли фамилии, чтобы избежать преследований, теряли паспорта, а метрические книги сгорали при бомбежках или изымались НКВД. 
                    </p>
                    <p>
                        Именно поэтому тот факт, что ваша семья последние 50 лет живет в России или Казахстане, <strong>никак не исключает</strong> того, что ваши прадеды могли быть рождены на территориях, попадающих под законы о репатриации стран Евросоюза (Румынии, Болгарии, Польши и других). Просто об этом не принято было говорить в советское время.
                    </p>

                    <div style="background: #f8fafc; border-radius: 12px; padding: 30px; margin: 40px 0; border: 1px solid #e2e8f0;">
                        <h3 style="color: #0B2046; margin-top: 0; font-family: 'Playfair Display', serif; font-size: 1.5rem;">Важная правовая норма</h3>
                        <p style="margin-bottom: 0;">
                            Закон не требует, чтобы вы <em>знали</em> о своих корнях или хранили старые свидетельства в домашнем комоде. Закон требует лишь предоставить документальное подтверждение из уполномоченных государственных архивов.
                        </p>
                    </div>

                    <h2 style="color: #0B2046; font-family: 'Playfair Display', serif; font-size: 2rem; margin: 40px 0 20px;">Как мы находим то, чего «нет»? (Механика поиска)</h2>
                    <p>
                        Мы не просим клиентов заниматься генеалогическим древом. <strong>Поиск легальных оснований — это фундамент нашей экспертной работы.</strong>
                    </p>
                    <p>
                        В штате EuroStatus работают профессиональные юристы-архивариусы, которые специализируются исключительно на восстановлении разорванных цепочек родства. Их алгоритм работы включает:
                    </p>
                    <ul style="list-style: none; padding: 0; margin: 25px 0;">
                        <li style="position: relative; padding-left: 30px; margin-bottom: 15px;">
                            <span style="position: absolute; left: 0; top: 6px; color: #CCA352;">
                                <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 11-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                            </span>
                            <strong>Глубокий аудит закрытых баз:</strong> Мы направляем официальные адвокатские запросы в ведомственные архивы ЗАГС стран СНГ, региональные архивы, суды и архивы Красного Креста.
                        </li>
                        <li style="position: relative; padding-left: 30px; margin-bottom: 15px;">
                            <span style="position: absolute; left: 0; top: 6px; color: #CCA352;">
                                <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 11-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                            </span>
                            <strong>Восстановление актовых записей:</strong> Если оригинальная запись утрачена, закон позволяет восстановить её через процедуру запроса в суд или профильные реестры. Это сложная и долгая процедура, которую наши адвокаты проводят полностью без вашего участия.
                        </li>
                        <li style="position: relative; padding-left: 30px; margin-bottom: 15px;">
                            <span style="position: absolute; left: 0; top: 6px; color: #CCA352;">
                                <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 11-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                            </span>
                            <strong>Формирование легальной связки:</strong> Мы по кирпичикам выстраиваем юридически безупречную линию: вы -> ваши родители -> бабушка/дедушка -> прабабушка/прадедушка.
                        </li>
                    </ul>

                    <h2 style="color: #0B2046; font-family: 'Playfair Display', serif; font-size: 2rem; margin: 40px 0 20px;">Никакого «фотошопа», только абсолютная легальность</h2>
                    <p>
                        Главный страх клиента — получить фальшивый документ. Министерства Юстиции европейских государств обладают прямыми протоколами для верификации любых иностранных выписок.
                    </p>
                    <p>
                        Любая попытка подать "нарисованную" справку мгновенно выявляется и заканчивается не просто отказом, а уголовным делом и вечным баном на въезд в ЕС.
                    </p>
                    <p>
                        <strong>Наша компания работает строго в правовом поле.</strong> Все документы, которые мы извлекаем из архивов, проходят строгую процедуру легализации. Они прошиваются, получают официальные печати, переводятся аккредитованными при Минюсте переводчиками и <strong>обязательно апостилируются</strong>. Апостиль — это международная гарантия подлинности документа, которую невозможно подделать.
                    </p>

                    <h2 style="color: #0B2046; font-family: 'Playfair Display', serif; font-size: 2rem; margin: 40px 0 20px;">Как мы гарантируем результат?</h2>
                    <p>
                        Процесс получения гражданства начинается не с предоплаты, а с бесплатного аудита.
                    </p>
                    <p>
                        Вы предоставляете нам лишь те крохи информации, которые у вас есть (ваше свидетельство о рождении, копии документов родителей). Наши юристы проводят первичный анализ. Если мы беремся за ваше дело и подписываем официальный договор — это значит, что мы <strong>на 100% уверены, что найдем легальные архивные основания</strong> для формирования вашего досье (DOSAR).
                    </p>
                    <p>
                        Вам не нужно гадать, есть ли у вас корни. Оставьте эту работу профессионалам.
                    </p>

                    <div style="margin-top: 50px; background: #0B2046; color: white; padding: 40px; border-radius: 16px; text-align: center;">
                        <h3 style="font-family: 'Playfair Display', serif; font-size: 1.8rem; margin-top: 0; margin-bottom: 15px;">Готовы проверить свои шансы?</h3>
                        <p style="opacity: 0.9; margin-bottom: 30px; font-size: 1.1rem; max-width: 600px; margin-left: auto; margin-right: auto;">
                            Свяжитесь с нами, и наш адвокат проведет первичный аудит вашей ситуации абсолютно конфиденциально и бесплатно.
                        </p>
                        <a href="/contact" style="display: inline-block; background: #CCA352; color: white; padding: 16px 35px; border-radius: 8px; font-weight: 600; text-decoration: none; font-size: 1.1rem; transition: all 0.3s;" onmouseover="this.style.background='#b88e40'" onmouseout="this.style.background='#CCA352'">
                            Оставить заявку на аудит
                        </a>
                    </div>
                </div>
            </article>
        </div>
    </main>

    <!-- FOOTER_PLACEHOLDER -->
</body>
</html>
"""

def build_article():
    with open('template.html', 'r', encoding='utf-8') as f:
        template = f.read()
    
    header_start = template.find('<!-- Unified Main Header -->')
    header_end = template.find('<!-- End Main Header -->') + len('<!-- End Main Header -->')
    header = template[header_start:header_end]
    
    with open('footer.txt', 'r', encoding='utf-8') as f:
        footer = f.read()

    final_html = html_content.replace('<!-- HEADER_PLACEHOLDER -->', header)
    final_html = final_html.replace('<!-- FOOTER_PLACEHOLDER -->', footer)

    with open('article-no-roots.html', 'w', encoding='utf-8') as f:
        f.write(final_html)

if __name__ == '__main__':
    build_article()
    print("article-no-roots.html successfully generated.")
