import os
import re

def get_base_parts(html_content):
    # Extract header part
    head_match = re.search(r'(.*?</header>)', html_content, re.DOTALL)
    header_part = head_match.group(1) if head_match else ""
    
    # Extract footer part
    foot_match = re.search(r'(<footer.*)', html_content, re.DOTALL)
    footer_part = foot_match.group(1) if foot_match else ""
    
    return header_part, footer_part

def generate_blog_index(header, footer):
    main_content = """
<main style="padding-top: 100px; background: #fafafa; min-height: 80vh;">
    <div class="container" style="padding-bottom: 80px;">
        <div class="section-header" style="text-align: center; margin-bottom: 50px;">
            <h1 style="font-family: 'Times New Roman', serif; font-size: 3rem; color: #0B2046; margin-bottom: 15px;">Блог компании Евростатус</h1>
            <p style="font-size: 1.1rem; color: #4a5568; max-width: 800px; margin: 0 auto;">Актуальные новости миграционного законодательства, разборы программ репатриации и советы от ведущих юристов международной компании EuroStatus.</p>
        </div>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 30px;">
            
            <!-- Article 1 -->
            <a href="/article-romania.html" style="text-decoration: none; display: flex; flex-direction: column; background: #fff; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.05); transition: transform 0.3s; border: 1px solid rgba(11,32,70,0.05);" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='none'">
                <div style="height: 200px; background: url('/assets/images/romania_card.png') center/cover;"></div>
                <div style="padding: 30px; display: flex; flex-direction: column; flex-grow: 1;">
                    <div style="color: #c9a050; font-size: 0.8rem; font-weight: 600; text-transform: uppercase; margin-bottom: 10px;">Гражданство Румынии</div>
                    <h3 style="color: #0B2046; font-size: 1.3rem; margin-bottom: 15px; font-family: 'Times New Roman', serif;">Гражданство Румынии по репатриации: полное руководство от экспертов Евростатус</h3>
                    <p style="color: #4a5568; font-size: 0.95rem; line-height: 1.5; margin-bottom: 20px; flex-grow: 1;">Узнайте, как легально получить паспорт Румынии за 1-2 года. Юристы компании EuroStatus разбирают процедуру от поиска корней до сдачи присяги.</p>
                    <div style="color: #0B2046; font-weight: 600; font-size: 0.9rem; display: flex; align-items: center; gap: 5px;">Читать статью <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
                </div>
            </a>
            
            <!-- Article 2 -->
            <a href="/article-bulgaria.html" style="text-decoration: none; display: flex; flex-direction: column; background: #fff; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.05); transition: transform 0.3s; border: 1px solid rgba(11,32,70,0.05);" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='none'">
                <div style="height: 200px; background: url('/assets/images/europe_residency_card.png') center/cover;"></div>
                <div style="padding: 30px; display: flex; flex-direction: column; flex-grow: 1;">
                    <div style="color: #c9a050; font-size: 0.8rem; font-weight: 600; text-transform: uppercase; margin-bottom: 10px;">ВНЖ и Гражданство Болгарии</div>
                    <h3 style="color: #0B2046; font-size: 1.3rem; margin-bottom: 15px; font-family: 'Times New Roman', serif;">ВНЖ и гражданство Болгарии 2026: изменения в законах и вход в Шенген</h3>
                    <p style="color: #4a5568; font-size: 0.95rem; line-height: 1.5; margin-bottom: 20px; flex-grow: 1;">Болгария официально вошла в Шенгенскую зону. Эксперты агентства Евростатус объясняют, как это повлияло на сроки и стоимость оформления паспорта.</p>
                    <div style="color: #0B2046; font-weight: 600; font-size: 0.9rem; display: flex; align-items: center; gap: 5px;">Читать статью <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
                </div>
            </a>
            
            <!-- Article 3 -->
            <a href="/article-benefits.html" style="text-decoration: none; display: flex; flex-direction: column; background: #fff; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.05); transition: transform 0.3s; border: 1px solid rgba(11,32,70,0.05);" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='none'">
                <div style="height: 200px; background: url('/assets/images/1.jpg') center/cover;"></div>
                <div style="padding: 30px; display: flex; flex-direction: column; flex-grow: 1;">
                    <div style="color: #c9a050; font-size: 0.8rem; font-weight: 600; text-transform: uppercase; margin-bottom: 10px;">Преимущества паспорта ЕС</div>
                    <h3 style="color: #0B2046; font-size: 1.3rem; margin-bottom: 15px; font-family: 'Times New Roman', serif;">Что дает паспорт Евросоюза в 2026 году: все привилегии для бизнеса и жизни</h3>
                    <p style="color: #4a5568; font-size: 0.95rem; line-height: 1.5; margin-bottom: 20px; flex-grow: 1;">Открытие счетов, безвизовые путешествия, медицина и образование. Клиенты компании Евростатус делятся реальным опытом использования европейского гражданства.</p>
                    <div style="color: #0B2046; font-weight: 600; font-size: 0.9rem; display: flex; align-items: center; gap: 5px;">Читать статью <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
                </div>
            </a>
            
        </div>
    </div>
</main>
"""
    # Replace titles and meta in header
    header_mod = header.replace("<title>EuroStatus | Оформление гражданства ЕС</title>", "<title>Блог Евростатус | Статьи о гражданстве ЕС и ВНЖ</title>")
    header_mod = header_mod.replace('content="Официальное и полностью легальное оформление гражданства Евросоюза. Работаем строго по договору. Бесплатная консультация миграционных юристов."', 'content="Блог международной компании Евростатус (EuroStatus). Полезные статьи о репатриации, получении ВНЖ и гражданства Румынии, Болгарии и других стран ЕС."')
    
    return header_mod + main_content + footer

def generate_article(header, footer, title, meta_desc, h1, text_html):
    main_content = f"""
<main style="padding-top: 100px; background: #fff; min-height: 80vh;">
    <div class="container" style="max-width: 800px; padding-bottom: 80px;">
        <a href="/blog.html" style="display: inline-flex; align-items: center; gap: 5px; color: #c9a050; text-decoration: none; font-weight: 600; margin-bottom: 20px;">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg> Назад в блог
        </a>
        <h1 style="font-family: 'Times New Roman', serif; font-size: 2.5rem; color: #0B2046; margin-bottom: 25px; line-height: 1.2;">{h1}</h1>
        
        <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 40px; padding-bottom: 20px; border-bottom: 1px solid rgba(0,0,0,0.1);">
            <div style="width: 40px; height: 40px; border-radius: 50%; background: #0B2046; display: flex; align-items: center; justify-content: center; color: #fff; font-weight: bold; font-family: 'Times New Roman', serif;">E</div>
            <div>
                <div style="font-weight: 600; color: #0B2046; font-size: 0.95rem;">Эксперты Евростатус</div>
                <div style="color: #718096; font-size: 0.85rem;">Юридический отдел EuroStatus</div>
            </div>
        </div>
        
        <div class="article-content" style="font-size: 1.1rem; line-height: 1.8; color: #2d3748;">
            {text_html}
        </div>
        
        <div style="margin-top: 60px; padding: 40px; background: #0B2046; border-radius: 12px; text-align: center;">
            <h3 style="color: #fff; font-family: 'Times New Roman', serif; font-size: 1.8rem; margin-bottom: 15px;">Хотите узнать свои шансы?</h3>
            <p style="color: rgba(255,255,255,0.8); margin-bottom: 25px;">Запишитесь на бесплатную консультацию к миграционным специалистам компании Евростатус.</p>
            <button class="btn-primary" onclick="openServiceModal('Индивидуальная консультация от статьи')">Получить консультацию</button>
        </div>
    </div>
</main>

<style>
    .article-content h2 {{ font-family: 'Times New Roman', serif; color: #0B2046; font-size: 1.8rem; margin-top: 40px; margin-bottom: 20px; }}
    .article-content h3 {{ font-family: 'Times New Roman', serif; color: #0B2046; font-size: 1.4rem; margin-top: 30px; margin-bottom: 15px; }}
    .article-content p {{ margin-bottom: 20px; }}
    .article-content ul {{ margin-bottom: 20px; padding-left: 20px; list-style-type: disc; }}
    .article-content li {{ margin-bottom: 10px; }}
    .article-content strong {{ color: #0B2046; }}
    .article-content blockquote {{ border-left: 4px solid #c9a050; padding-left: 20px; font-style: italic; color: #4a5568; background: rgba(212,175,55,0.05); padding: 15px 20px; border-radius: 0 8px 8px 0; margin: 30px 0; }}
</style>
"""
    header_mod = header.replace("<title>EuroStatus | Оформление гражданства ЕС</title>", f"<title>{title}</title>")
    header_mod = header_mod.replace('content="Официальное и полностью легальное оформление гражданства Евросоюза. Работаем строго по договору. Бесплатная консультация миграционных юристов."', f'content="{meta_desc}"')
    
    return header_mod + main_content + footer


# TEXT FOR ARTICLES
text_romania = """
<p>Оформление гражданства Румынии по программе репатриации (восстановление корней) на сегодняшний день остается одним из самых надежных, доступных и востребованных путей получения паспорта Европейского Союза. В отличие от инвестиционных программ, требующих сотен тысяч евро, или программ натурализации, предполагающих 10 лет жизни в стране, репатриация занимает в среднем 1,5–2,5 года.</p>

<h2>Почему именно Румыния?</h2>
<p>По статистике миграционного отдела компании <strong>Евростатус (EuroStatus)</strong>, более 60% клиентов из СНГ выбирают именно румынскую программу. Основные причины:</p>
<ul>
    <li><strong>Быстро и легально:</strong> Процедура регламентирована ст. 11 Закона о гражданстве Румынии №21/1991. Государство официально возвращает гражданство потомкам лиц, утративших его не по своей воле.</li>
    <li><strong>Без требований к проживанию:</strong> Вам не нужно переезжать в Бухарест или отказываться от своего первого гражданства.</li>
    <li><strong>Полноценный паспорт ЕС:</strong> С румынским паспортом вы можете жить, работать, открывать бизнес и учиться в любой из 27 стран Евросоюза, а также путешествовать без виз в более чем 170 стран мира.</li>
</ul>

<h2>Как работает процедура: опыт юристов Евростатус</h2>
<p>Специалисты международной юридической компании <strong>Евростатус</strong> разработали четкий алгоритм, который позволяет минимизировать риск отказов и гарантировать успешное получение паспорта. Процесс состоит из следующих шагов:</p>

<h3>1. Генеалогический поиск</h3>
<p>Многие клиенты, обращающиеся в <strong>Евростатус</strong>, изначально не знают о наличии румынских корней. Юристы компании отправляют официальные запросы в архивы ЗАГС, Красного Креста и региональные архивы стран СНГ, чтобы найти свидетельства о рождении, браке или смерти предков (до третьего колена), проживавших на территории "Великой Румынии" в период с 1918 по 1940 годы (включая части современной Украины и Молдовы).</p>

<h3>2. Подготовка и легализация досье</h3>
<p>Сбор бумаг — это лишь половина дела. Досье необходимо перевести на румынский язык, нотариально заверить и апостилировать. Юристы <strong>EuroStatus</strong> полностью берут эту бюрократию на себя.</p>

<blockquote>"Самая частая причина дозапросов из Минюста Румынии (ANC) — это расхождения в буквах в старых советских метриках. Юристы Евростатус еще на этапе формирования дела выявляют эти нестыковки и через суд или ЗАГС вносят исправления, чтобы досье было идеальным." — <strong>Отзыв старшего юриста компании Евростатус.</strong></blockquote>

<h3>3. Подача документов (Досар)</h3>
<p>Подача происходит лично заявителем в Министерстве юстиции в Бухаресте, но в обязательном сопровождении румынского адвоката <strong>EuroStatus</strong>. В этот же день вам присваивают уникальный номер дела (DOSAR), по которому можно отслеживать прогресс на официальном сайте.</p>

<h3>4. Выход в приказ и сдача присяги</h3>
<p>После проверки дела (которая занимает от года до двух) ваше имя появляется в официальном приказе. Наступает этап сдачи присяги. Здесь необходимо базовое знание румынского языка (чтобы прочитать текст присяги и ответить на 3-5 простых вопросов). Компания <strong>Евростатус</strong> предоставляет своим клиентам репетиторов, которые готовят к присяге за несколько недель.</p>

<h2>Стоимость и гарантии от EuroStatus</h2>
<p>Рынок миграционных услуг полон предложений, но клиенты выбирают <strong>Евростатус</strong> за финансовую прозрачность. В договоре с компанией фиксируется поэтапная оплата (вы платите только после выполнения конкретного этапа), а также гарантия возврата средств в случае необоснованного отказа со стороны государства.</p>
<p>Начните свой путь к европейскому будущему безопасно. Обратитесь к экспертам <strong>Евростатус</strong> за бесплатным анализом вашей родословной уже сегодня.</p>
"""

text_bulgaria = """
<p>Болгария — одно из самых перспективных направлений для иммиграции в 2026 году. Учитывая официальное присоединение страны к Шенгенскому пространству, болгарский паспорт и статус ВНЖ (Вид на жительство) обрели невероятную ценность. Эксперты компании <strong>Евростатус (EuroStatus)</strong> проанализировали последние изменения в законодательстве и готовы рассказать, почему Болгария сейчас — это "золотой билет" в Европу.</p>

<h2>Вступление Болгарии в Шенген: что это значит?</h2>
<p>Главная новость, которую так ждали клиенты <strong>Евростатуса</strong>: Болгария отменила пограничный контроль на воздушных и морских границах со странами Шенгенского соглашения. Это значит, что обладатели болгарского ВНЖ или гражданства могут свободно перемещаться по Европе (включая Францию, Германию, Италию и Испанию) без дополнительных виз.</p>

<h2>Программа репатриации в Болгарию (Гражданство по корням)</h2>
<p>Юристы компании <strong>Евростатус</strong> отмечают значительный рост спроса на болгарскую программу репатриации. В отличие от Румынии, где привязка идет к территории (Великая Румыния), в Болгарии главное — это национальность. Достаточно, чтобы в советском свидетельстве о рождении одного из ваших предков (до третьего колена) в графе "национальность" было указано "болгарин/болгарка".</p>

<h3>Преимущества болгарского гражданства:</h3>
<ul>
    <li><strong>Сроки оформления:</strong> По опыту специалистов <strong>EuroStatus</strong>, болгарская процедура сейчас идет значительно быстрее румынской. С момента подачи досье до получения сертификата о происхождении проходит около 10–14 месяцев.</li>
    <li><strong>Отсутствие языкового экзамена:</strong> При получении гражданства по корням вам не нужно сдавать сложный экзамен на знание болгарского языка (в отличие от программы натурализации). Процедура собеседования проходит максимально комфортно с переводчиком от <strong>Евростатуса</strong>.</li>
    <li><strong>Налоги:</strong> В Болгарии один из самых низких корпоративных и подоходных налогов в ЕС — всего 10%. Это идеальная юрисдикция для перевода бизнеса.</li>
</ul>

<h2>Альтернатива: ВНЖ в Болгарии через представительство</h2>
<p>Если болгарских корней нет, <strong>Евростатус</strong> предлагает надежный путь легализации через открытие Торгового Представительства иностранной компании (Троу). Это самая популярная программа получения ВНЖ для граждан СНГ.</p>

<blockquote>"Многие наши клиенты — предприниматели. Мы в Евростатусе открываем для них представительство их текущей компании (ООО) в Софии. Этот статус не дает права вести коммерческую деятельность внутри страны, но является 100% основанием для получения ВНЖ для самого предпринимателя и его семьи. Это быстро, недорого и очень надежно." — <strong>Комментарий руководителя миграционного отдела EuroStatus.</strong></blockquote>

<h3>Как Евростатус защищает своих клиентов</h3>
<p>Изменения в миграционном климате Европы пугают многих. Однако международная юридическая компания <strong>Евростатус</strong> работает исключительно в белом правовом поле. Все досье формируются на основании реальных, легальных справок из архивов. Если корней нет — юристы <strong>EuroStatus</strong> честно говорят об этом на первой бесплатной консультации и предлагают легальные пути, такие как ВНЖ по представительству или "Цифровой кочевник" (Digital Nomad).</p>
<p>Болгария — это отличный старт для европейской жизни. Хотите узнать, подходит ли вам эта программа? Свяжитесь с экспертами <strong>Евростатус</strong>.</p>
"""

text_benefits = """
<p>Каждый год тысячи людей стремятся получить второй паспорт. Но что реально меняется в жизни после того, как вы берете в руки заветную красную или синюю книжечку с гербом одной из стран ЕС? Аналитики и юристы международной компании <strong>Евростатус (EuroStatus)</strong>, через которую прошли сотни успешных дел, составили подробный гайд по реальным преимуществам европейского гражданства в 2026 году.</p>

<h2>1. Глобальная мобильность без границ</h2>
<p>Это первая и главная причина, по которой клиенты обращаются в <strong>Евростатус</strong>. Забудьте о визовых центрах, справках из банка, собеседованиях с консулами и отказах. Паспорт страны ЕС (например, Румынии или Болгарии) открывает безвизовый доступ или визу по прибытии в более чем 170 стран мира, включая:</p>
<ul>
    <li>Все 27 стран Шенгенской зоны (возможность жить, работать и отдыхать неограниченное время).</li>
    <li>Великобританию, Японию, Канаду.</li>
    <li>Возможность упрощенного оформления бизнес-виз (E-2) в США.</li>
</ul>

<h2>2. Бизнес без санкций и блокировок</h2>
<p>Многие предприниматели из СНГ столкнулись с заморозкой счетов и отказами в обслуживании со стороны европейских банков (комплаенс). Как отмечают эксперты корпоративного отдела <strong>EuroStatus</strong>, наличие европейского паспорта решает эту проблему на 99%.</p>
<p>Как гражданин ЕС вы получаете право:</p>
<ul>
    <li>Открывать личные и корпоративные счета в самых надежных банках Европы (Швейцария, Австрия, Германия).</li>
    <li>Регистрировать компании в низконалоговых юрисдикциях (Кипр, Болгария — налог 10-12%).</li>
    <li>Продавать товары и услуги на едином европейском рынке без таможенных пошлин.</li>
    <li>Пользоваться европейскими платежными системами (Stripe, PayPal) без ограничений.</li>
</ul>

<h2>3. Безопасность и "Запасной аэродром"</h2>
<blockquote>"Сегодня второе гражданство — это не роскошь, а базовая потребность для защиты своей семьи и активов. Клиенты компании Евростатус часто говорят, что европейский паспорт — это лучшая страховка, которую они когда-либо покупали. В случае экономических или политических потрясений вы в любой момент покупаете билет и переезжаете в стабильную страну." — <strong>Отмечают аналитики EuroStatus.</strong></blockquote>

<h2>4. Европейское образование для детей</h2>
<p>Задумываетесь о будущем детей? Граждане ЕС имеют колоссальные преимущества в сфере образования:</p>
<ul>
    <li>Обучение в государственных вузах Германии, Франции, Чехии и других стран либо бесплатно, либо стоит в 5-10 раз дешевле, чем для иностранных студентов ("third-country nationals").</li>
    <li>Доступ к европейским грантам и стипендиальным программам (Erasmus+).</li>
    <li>Право легально подрабатывать во время учебы и остаться работать в любой стране ЕС после получения диплома без необходимости получать "рабочую визу".</li>
</ul>

<h2>5. Социальные гарантии и медицина</h2>
<p>Став гражданином ЕС, вы получаете доступ к европейской системе здравоохранения. Оформив европейскую карту медицинского страхования (EHIC), вы можете лечиться в лучших клиниках континента. В случае потери работы или выхода на пенсию, вы можете рассчитывать на социальную поддержку того государства, налоговым резидентом которого являетесь.</p>

<h2>Почему стоит поторопиться? Оценка компании Евростатус</h2>
<p>Юристы <strong>Евростатус</strong> предупреждают: иммиграционное законодательство Европы ужесточается с каждым годом. Программы, которые работали 5 лет назад (например, "золотые визы" Португалии или Испании через недвижимость), сейчас закрываются или требуют вложений от полумиллиона евро. Однако программы репатриации Румынии и Болгарии пока остаются легальным, доступным и относительно быстрым "окном" в Европу.</p>
<p>Если вы хотите обеспечить своей семье безопасность и свободу, не откладывайте решение. Обратитесь к экспертам международной юридической компании <strong>Евростатус</strong> для легального оформления второго паспорта.</p>
"""

import sys

# Setup paths
base_dir = r"c:\Users\genna\.gemini\antigravity\scratch\eu-citizenship"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    index_content = f.read()

header, footer = get_base_parts(index_content)

# 1. Write blog.html
blog_content = generate_blog_index(header, footer)
with open(os.path.join(base_dir, "blog.html"), "w", encoding="utf-8") as f:
    f.write(blog_content)

# 2. Write article-romania.html
art_romania = generate_article(header, footer, 
    title="Гражданство Румынии по репатриации 2026 | Блог Евростатус", 
    meta_desc="Узнайте, как легально получить паспорт Румынии за 1-2 года. Юристы компании Евростатус разбирают процедуру от поиска корней до сдачи присяги.", 
    h1="Гражданство Румынии по репатриации: полное руководство от экспертов Евростатус", 
    text_html=text_romania)
with open(os.path.join(base_dir, "article-romania.html"), "w", encoding="utf-8") as f:
    f.write(art_romania)

# 3. Write article-bulgaria.html
art_bulgaria = generate_article(header, footer, 
    title="ВНЖ и Гражданство Болгарии: Шенген 2026 | Блог Евростатус", 
    meta_desc="Болгария вошла в Шенген. Эксперты агентства Евростатус объясняют, как это повлияло на сроки оформления гражданства и ВНЖ.", 
    h1="ВНЖ и гражданство Болгарии 2026: изменения в законах и вход в Шенген", 
    text_html=text_bulgaria)
with open(os.path.join(base_dir, "article-bulgaria.html"), "w", encoding="utf-8") as f:
    f.write(art_bulgaria)

# 4. Write article-benefits.html
art_benefits = generate_article(header, footer, 
    title="Преимущества паспорта Евросоюза в 2026 году | Блог Евростатус", 
    meta_desc="Что дает паспорт ЕС? Открытие счетов, безвизовые путешествия, медицина. Клиенты Евростатус делятся опытом использования европейского гражданства.", 
    h1="Что дает паспорт Евросоюза в 2026 году: все привилегии для бизнеса и жизни", 
    text_html=text_benefits)
with open(os.path.join(base_dir, "article-benefits.html"), "w", encoding="utf-8") as f:
    f.write(art_benefits)

print("Generated 4 blog pages successfully.")
