import os

def create_legal_pages():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    header_end = html.find('<main>')
    if header_end == -1:
        print("Could not find <main>")
        return
        
    footer_start = html.find('<!-- Main Footer -->')
    if footer_start == -1:
        print("Could not find footer")
        return
        
    header = html[:header_end]
    footer = html[footer_start:]
    
    # Extract the script tags from the bottom of index.html that we might want
    # Footer already contains them!
    
    # Fix the title and add legal styles to header
    header_privacy = header.replace('<title>EuroStatus | Оформление гражданства ЕС</title>', '<title>EuroStatus | Политика конфиденциальности</title>')
    header_privacy = header_privacy.replace('</head>', '''
<style>
.legal-content { max-width: 900px; margin: 120px auto 80px auto; padding: 0 20px; color: #1a202c; }
.legal-content h1 { font-family: 'Times New Roman', serif; color: #0B2046; font-size: 2.5rem; margin-bottom: 30px; }
.legal-content h2 { font-family: 'Times New Roman', serif; color: #0B2046; font-size: 1.8rem; margin-top: 40px; margin-bottom: 20px; }
.legal-content p { font-size: 1.05rem; line-height: 1.6; margin-bottom: 20px; color: #4a5568; }
.legal-content ul { padding-left: 20px; margin-bottom: 20px; color: #4a5568; }
.legal-content li { margin-bottom: 10px; line-height: 1.6; }
</style>
</head>''')

    header_terms = header.replace('<title>EuroStatus | Оформление гражданства ЕС</title>', '<title>EuroStatus | Условия использования</title>')
    header_terms = header_terms.replace('</head>', '''
<style>
.legal-content { max-width: 900px; margin: 120px auto 80px auto; padding: 0 20px; color: #1a202c; }
.legal-content h1 { font-family: 'Times New Roman', serif; color: #0B2046; font-size: 2.5rem; margin-bottom: 30px; }
.legal-content h2 { font-family: 'Times New Roman', serif; color: #0B2046; font-size: 1.8rem; margin-top: 40px; margin-bottom: 20px; }
.legal-content p { font-size: 1.05rem; line-height: 1.6; margin-bottom: 20px; color: #4a5568; }
.legal-content ul { padding-left: 20px; margin-bottom: 20px; color: #4a5568; }
.legal-content li { margin-bottom: 10px; line-height: 1.6; }
</style>
</head>''')

    privacy_content = """
<main>
<div class="legal-content">
<h1>Политика конфиденциальности</h1>
<p>Последнее обновление: 23 апреля 2026 г.</p>

<p>Настоящая Политика конфиденциальности (далее — «Политика») описывает, как A.S. CONSULTING COMPANY S.R.L. (далее — «Мы», «Компания») собирает, использует и защищает вашу личную информацию в соответствии с Общим регламентом по защите данных (GDPR) ЕС.</p>

<h2>1. Какую информацию мы собираем</h2>
<p>Мы можем собирать следующие категории персональных данных:</p>
<ul>
<li><strong>Идентификационные данные:</strong> имя, фамилия, дата рождения, паспортные данные.</li>
<li><strong>Контактные данные:</strong> адрес электронной почты, номер телефона, физический адрес.</li>
<li><strong>Данные о происхождении:</strong> метрики, свидетельства о рождении, браке и смерти предков для процессов репатриации.</li>
<li><strong>Финансовые данные:</strong> информация, необходимая для инвестиционных программ или подтверждения легальности доходов.</li>
</ul>

<h2>2. Как мы используем ваши данные</h2>
<p>Ваши данные используются исключительно для следующих целей:</p>
<ul>
<li>Оказание юридических услуг по оформлению гражданства, ВНЖ и ПМЖ.</li>
<li>Анализ генеалогического древа и истребование документов в архивах.</li>
<li>Связь с вами для предоставления консультаций и обновления статуса вашего дела.</li>
<li>Выполнение требований европейского и международного законодательства.</li>
</ul>

<h2>3. Защита и хранение данных</h2>
<p>Мы внедряем передовые технические и организационные меры для защиты ваших данных от несанкционированного доступа. Все документы хранятся на защищенных серверах на территории Европейского Союза. Мы не передаем вашу информацию третьим лицам без вашего явного письменного согласия, за исключением случаев, когда это прямо требуется для подачи вашего досье в государственные органы (например, Министерство Юстиции).</p>

<h2>4. Ваши права (GDPR)</h2>
<p>В соответствии с GDPR, вы имеете право:</p>
<ul>
<li>Запросить доступ к вашим персональным данным.</li>
<li>Потребовать исправления неточных или неполных данных.</li>
<li>Потребовать удаления ваших данных («право быть забытым»), если это не противоречит нашим юридическим обязательствам.</li>
<li>Ограничить или отозвать согласие на обработку данных.</li>
</ul>

<h2>5. Контакты по вопросам конфиденциальности</h2>
<p>Если у вас есть вопросы относительно нашей Политики конфиденциальности или вы хотите воспользоваться своими правами, пожалуйста, свяжитесь с нами:</p>
<p><strong>A.S. CONSULTING COMPANY S.R.L.</strong><br>
Адрес: Jud. Constanța, Mun. Constanța, Str. Eliberării, Nr. 25<br>
Email: <a href="mailto:eurostatus@ro.ru">eurostatus@ro.ru</a></p>
</div>
</main>
"""

    terms_content = """
<main>
<div class="legal-content">
<h1>Условия использования</h1>
<p>Последнее обновление: 23 апреля 2026 г.</p>

<p>Добро пожаловать на веб-сайт EuroStatus, принадлежащий <strong>A.S. CONSULTING COMPANY S.R.L.</strong>. Посещая и используя наш веб-сайт, вы принимаете настоящие Условия использования. Если вы не согласны с какими-либо из этих условий, пожалуйста, прекратите использование сайта.</p>

<h2>1. Общие положения</h2>
<p>Веб-сайт EuroStatus предоставляет информацию об услугах в сфере иммиграционного консалтинга, оформления гражданства, ВНЖ и ПМЖ в ЕС и других странах. Материалы на этом сайте носят исключительно информационный характер и не являются юридической консультацией.</p>

<h2>2. Интеллектуальная собственность</h2>
<p>Все материалы, опубликованные на сайте, включая тексты, графику, логотипы, дизайн и структуру (за исключением контента, принадлежащего третьим лицам), являются собственностью A.S. CONSULTING COMPANY S.R.L. Копирование, распространение или использование любых материалов без письменного разрешения строго запрещено.</p>

<h2>3. Предоставление услуг</h2>
<p>Оказание юридических и консалтинговых услуг осуществляется только на основании официально заключенного договора между Клиентом и Компанией. Условия, описанные на веб-сайте (включая цены, сроки и гарантии), могут уточняться или изменяться в рамках индивидуального договора в зависимости от специфики конкретного дела.</p>

<h2>4. Гарантии и ответственность</h2>
<p>Мы прилагаем все усилия для обеспечения актуальности и точности информации на сайте. Однако иммиграционное законодательство стран регулярно меняется, поэтому мы не гарантируем, что вся предоставленная информация является исчерпывающей и применимой к вашему конкретному случаю на момент прочтения. A.S. CONSULTING COMPANY S.R.L. не несет ответственности за любой ущерб, возникший в результате использования информации с данного сайта.</p>

<h2>5. Ссылки на сторонние ресурсы</h2>
<p>Наш сайт может содержать ссылки на сторонние веб-сайты. Мы не контролируем эти ресурсы и не несем ответственности за их содержание или политику конфиденциальности. Переход по ссылкам осуществляется на ваш собственный риск.</p>

<h2>6. Изменения условий</h2>
<p>Мы оставляем за собой право вносить изменения в настоящие Условия использования в любое время без предварительного уведомления. Продолжение использования сайта после публикации изменений означает их принятие.</p>

<h2>7. Юридическая информация и контакты</h2>
<p><strong>A.S. CONSULTING COMPANY S.R.L.</strong><br>
Код регистрации (CUI): 17839407<br>
Адрес: Jud. Constanța, Mun. Constanța, Str. Eliberării, Nr. 25, Romania<br>
Email для связи: <a href="mailto:support@eurostatus.com">support@eurostatus.com</a></p>
</div>
</main>
"""

    with open('privacy.html', 'w', encoding='utf-8') as f:
        f.write(header_privacy + privacy_content + footer)

    with open('terms.html', 'w', encoding='utf-8') as f:
        f.write(header_terms + terms_content + footer)

create_legal_pages()
