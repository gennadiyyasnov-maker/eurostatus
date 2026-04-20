import re

file_path = 'index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_section = """<!-- Legal Guarantees Section -->
<section class="guarantees-section" style="padding: 100px 0; background: #fafafa; position: relative; overflow: hidden;">
  <!-- Decor shape -->
  <div style="position: absolute; top: 0; left: 0; right: 0; height: 1px; background: linear-gradient(90deg, transparent, rgba(11,32,70,0.1), transparent);"></div>
  
  <div class="container relative z-10">
    <div class="section-header text-center" style="max-width: 800px; margin: 0 auto 60px auto;">
      <span style="color: #c9a050; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 2px; font-weight: 600; display: block; margin-bottom: 10px;">Мы знаем, о чем вы переживаете</span>
      <h2 style="font-size: 2.8rem; color: #0B2046; font-family: 'Times New Roman', serif;">Снимаем главные страхи</h2>
      <p style="font-size: 1.1rem; color: #4a5568;">Оформление гражданства — это риск. Мы не прячемся за общими фразами «индивидуальный подход» и прямо говорим о том, как решаем проблемы, которые боятся обсуждать в других агентствах.</p>
    </div>

    <div style="display: flex; flex-direction: column; gap: 20px; max-width: 900px; margin: 0 auto;">
      
      <!-- Card 1 -->
      <div style="background: #ffffff; border-radius: 12px; padding: 40px; border-left: 6px solid #c9a050; box-shadow: 0 10px 30px rgba(0,0,0,0.03); transition: transform 0.3s ease;" class="hover-up">
        <div style="display: flex; gap: 30px; align-items: flex-start;">
          <div style="flex-shrink: 0; margin-top: 5px;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#c9a050" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
              <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
            </svg>
          </div>
          <div>
            <div style="color: #e53e3e; font-weight: 600; font-size: 0.95rem; margin-bottom: 10px; display: inline-flex; align-items: center; gap: 8px; background: rgba(229, 62, 62, 0.1); padding: 4px 12px; border-radius: 20px;">
               Боль: Отдать деньги «в никуда» и получить скрытые платежи
            </div>
            <h3 style="color: #0B2046; font-size: 1.5rem; font-family: 'Times New Roman', serif; margin-bottom: 15px;">Только поэтапная оплата за результат</h3>
            <p style="color: #4a5568; line-height: 1.6; margin: 0;">Мы не требуем 100% предоплату. Вы платите частями, исключительно по факту прохождения каждого юридического этапа. Итоговая сумма железно фиксируется в договоре «на берегу» — ни одной непредвиденной комиссии за весь срок ведения дела.</p>
          </div>
        </div>
      </div>

      <!-- Card 2 -->
      <div style="background: #ffffff; border-radius: 12px; padding: 40px; border-left: 6px solid #0B2046; box-shadow: 0 10px 30px rgba(0,0,0,0.03); transition: transform 0.3s ease;" class="hover-up">
        <div style="display: flex; gap: 30px; align-items: flex-start;">
          <div style="flex-shrink: 0; margin-top: 5px;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#0B2046" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
               <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
            </svg>
          </div>
          <div>
            <div style="color: #e53e3e; font-weight: 600; font-size: 0.95rem; margin-bottom: 10px; display: inline-flex; align-items: center; gap: 8px; background: rgba(229, 62, 62, 0.1); padding: 4px 12px; border-radius: 20px;">
               Риск: Получить отказ и испортить визовую историю навсегда
            </div>
            <h3 style="color: #0B2046; font-size: 1.5rem; font-family: 'Times New Roman', serif; margin-bottom: 15px;">Только 100% законная прозрачная репатриация</h3>
            <p style="color: #4a5568; line-height: 1.6; margin: 0;">Мы не восстанавливаем корни "из воздуха" и не используем поддельные справки. Если вы не имеете законных оснований — мы откажем вам еще на первичном аудите. Все документы проходят трехкратную закрытую независимую проверку перед подачей в Минюст.</p>
          </div>
        </div>
      </div>

      <!-- Card 3 -->
      <div style="background: #ffffff; border-radius: 12px; padding: 40px; border-left: 6px solid #c9a050; box-shadow: 0 10px 30px rgba(0,0,0,0.03); transition: transform 0.3s ease;" class="hover-up">
        <div style="display: flex; gap: 30px; align-items: flex-start;">
          <div style="flex-shrink: 0; margin-top: 5px;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#c9a050" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
               <path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path>
               <line x1="1" y1="1" x2="23" y2="23"></line>
            </svg>
          </div>
          <div>
            <div style="color: #e53e3e; font-weight: 600; font-size: 0.95rem; margin-bottom: 10px; display: inline-flex; align-items: center; gap: 8px; background: rgba(229, 62, 62, 0.1); padding: 4px 12px; border-radius: 20px;">
               Риск: О втором гражданстве узнают гос. структуры вашей страны
            </div>
            <h3 style="color: #0B2046; font-size: 1.5rem; font-family: 'Times New Roman', serif; margin-bottom: 15px;">Полный информационный вакуум</h3>
            <p style="color: #4a5568; line-height: 1.6; margin: 0;">Ваши личные данные обрабатываются исключительно на территории Румынии и строго контролируются европейским регламентом GDPR. Никакие запросы из вашей текущей страны пребывания не смогут заставить ЕС раскрыть информацию о получении вами статуса резидента.</p>
          </div>
        </div>
      </div>

      <!-- Card 4 -->
      <div style="background: #ffffff; border-radius: 12px; padding: 40px; border-left: 6px solid #0B2046; box-shadow: 0 10px 30px rgba(0,0,0,0.03); transition: transform 0.3s ease;" class="hover-up">
        <div style="display: flex; gap: 30px; align-items: flex-start;">
          <div style="flex-shrink: 0; margin-top: 5px;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#0B2046" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
               <circle cx="12" cy="12" r="10"></circle>
               <polyline points="12 6 12 12 16 14"></polyline>
            </svg>
          </div>
          <div>
            <div style="color: #e53e3e; font-weight: 600; font-size: 0.95rem; margin-bottom: 10px; display: inline-flex; align-items: center; gap: 8px; background: rgba(229, 62, 62, 0.1); padding: 4px 12px; border-radius: 20px;">
               Опасение: Бюрократический ад и затягивание процесса на годы
            </div>
            <h3 style="color: #0B2046; font-size: 1.5rem; font-family: 'Times New Roman', serif; margin-bottom: 15px;">Адвокаты делают 95% рутинной работы за вас</h3>
            <p style="color: #4a5568; line-height: 1.6; margin: 0;">Мы прописываем жесткие дедлайны по каждому этапу подготовки дела прямо в договоре. Вы не общаетесь с чиновниками и не стоите в очередях. Ваше физическое присутствие потребуется ровно дважды — на торжественной присяге и для подачи документов.</p>
          </div>
        </div>
      </div>

    </div>
  </div>
  
  <style>
    .hover-up:hover {
      transform: translateY(-5px);
      box-shadow: 0 15px 35px rgba(0,0,0,0.06) !important;
    }
  </style>
</section>"""

# Using regex to replace the section from <!-- Legal Guarantees Section --> up to <!-- Process Section -->
pattern = re.compile(r'<!-- Legal Guarantees Section -->.*?<!-- Process Section -->', re.DOTALL)
content = re.sub(pattern, new_section + "\n<!-- Process Section -->", content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
