#!/usr/local/bin/python
# coding: utf-8

S_A1_B1_C1_D1_E1_F1_G1_H1_I1_J1 = 'На графике все точки находятся на высоком уровне, но человек не находится в этой ' \
                                  'реальности - такой график называется "тити-вити". "Безмятежность" (но человек не ' \
                                  'может быть лицом к лицу с МЭСТ или любыми недочетами). Этот человек полностью ' \
                                  'подавлен как тэтан.'
S1 = 'Случайный график. Такой график получается, когда человек отвечает на вопросы теста ОСА случайным образом. ' \
     'Либо он не понял вопросы, либо его не интересовал этот тест, но человек отвечал на вопросы случайным образом и ' \
     'про этот тест сказать больше нечего.'
S_G90_I90 = 'Комплекс мученика или преследуемого. Возможно человек лжет.'
S_A1_B34 = 'Вы несчастны и депрессивны, и Ваш взгляд на жизнь пессимистичен. Проблем и трудностей так много, что Вы ' \
           'не в состоянии с ними справиться. Они заставляют Вас быть надостаточно разумным и надежным, а кроме ' \
           'того, они воздействуют на Вашу способность сосредотачиваться, хотя Вы можете считать разумность, ' \
           'надежность и способность сосредотачиваться своими лучшими качествами. Именно по этой причине Ваша семья ' \
           'и Ваши друзья считают, что им трудно нахозиться рядом с Вами.'
S_A1_C34 = 'Вы раздражительны и чрезмерно возбудимы. Ваше беспокойство и возбуждение оказывает негативный эффект ' \
           'не только на других, но и на Вас самих. Ваша неспособность расслабиться и нервозное состояние приводят ' \
           'Вас к нестабильному состоянию, уменьшают Вашу способность концентрироваться и заставляют Вас быть ' \
           'ненадежным в Ваших решениях и недостаточно разумным, даже если Вам хочется думать, что с этими чертами ' \
           'у Вас все в порядке.'
S_B1_A34 = 'Поскольку у Вас есть трудности с концентрацией Вашего внимания, а Ваш характер нестабильный и ' \
           'импульсивный, Вы не такой счастливый человек, каким Вы считаете себя или каким Вы хотите быть. ' \
           'Окружающих расстраивают такие Ваши качества как ненадежность, неверность, а также то, что они не могут ' \
           'положиться на Вас. В свете этого, Ваш энтузиазм и интерес к жизни на самом деле меньше и слабее.'
S_B1_C34 = 'Вам не хватает спокойствия и способности расслабиться, что приводит к тому, что Вы на самом деле менее ' \
           'счастливы, чем Вы, как правило, считаете. Ваши нервные привычки снижают Ваш энтузиазм и интерес к ' \
           'жизни больше, чем Вы полагаете. Вы слишком легко приходите во взволнованное и раздражительное состояние, ' \
           'для того чтобы поддерживать в себе действительно счастливое и оптимистичное расположение духа. Ваше ' \
           'хорошее настроение легко портится такой Вашей нервозностью.'
S_C1_A34 = 'Вы нестабильны и рассеяны. Вы очень слабо контролируете свое внимание, которое легко рассеивается или ' \
           'фиксируется на каком-нибудь отдельном препятствии. Поэтому Вы не настолько хорошо владеете собой, как Вы ' \
           'хотели бы, чтобы о Вас думали другие люди. Ваше спокойствие - это просто маска, за которой Вы хотите ' \
           'спрятать Вашу нестабильность и ненадежность.'
S_C1_B34 = 'Вы ни в коей мере не довольны жизнью. Она заставляет Вас быть гораздо более нервозным, чем Вы сами ' \
           'хотели бы быть. Проблемы и трудности, являющиеся причиной Вашей депрессии, очень сильно расстраивают ' \
           'Вас, и Вы отчаянно пытаетесь скрыть это под маской внешнего спокойствия и безмятежности. Ваши попытки ' \
           'сохранить эту маску спокойствия потерпят полную неудачу, если только причины Ваших несчастий не будут ' \
           'устренены.'
S_D1_A34 = 'У Вас нестабильный характер и Вы слишком импульсивны и рассеяны. Вы не способны сосредотачивать свое ' \
           'внимание, которое либо блуждает, либо компульсивно фиксируется на чем-то. Вы ошибочно считаете себя ' \
           'надежным человеком, но такакя надежность и уверенность основаны на гипнотических решениях, суждениях ' \
           'и мнениях, которые Вы не можете контролировать или не способны изменять.'
S_E1_D34 = 'Вы ненадежны и не верите в себя. На самом деле Вы не можете решить для себя, какие цели Вы хотите ' \
           'достичь, а какие - нет, хотя Вы достаточно активны. Не все Ваши действия в действительности ' \
           'контролируются Вами, потому что Вы в действительности не знаете, чего Вы хотите достичь, делая что-то. ' \
           'Вы чувствуете, что для Вас лучше делать что-нибудь, чем ничего не делать, но такакя бесцельная ' \
           'деятельность создаст Вам трудности.'
S_E1_F34 = 'Вы замкнутый и покорный человек. Вы боитесь иметь дело с людьми и сталкиваться с какими-нибудь ' \
           'ситуациями в открытую - только скрытно. Это создаст для Вас много трудностей. То, что Вы настолько ' \
           'активны, но в то же время достаточно замкнуты, говорит о том ,что Вы делаете вещи, с которыми на самом ' \
           'деле не можете справиться. В будущем это принесет Вам очень много трудностей.'
S_F1_E34 = 'Вы не очень активны, Вы испытываете тружности с тем, чтобы начать какие-либо действия и продолжать их, ' \
           'когда они уже начаты, однако, Вы достаточно способны и открыто можете контролировать людей и ситуации. ' \
           'Следовательно, из-за Вашей обычной лени Вы не делаете всего того, что Вы реально способны делать, и ' \
           'растрачиваете свои таланты.'
S_F1_G34 = 'Вы безответственны в жизни и в работе. Вы обвиняете других в том, что происходит с Вами, и не будете ' \
           'признавать никаких мнений о том, чот Вы должны иметь какую бы то ни было ответственность за то, что с ' \
           'Вами происходит или произойдет. Тот факт, что Вы достаточно способны и открыты и тем не менее настолько ' \
           'безответственны, говорит о том, что Вы способны совершать действия, не заботясь о последствиях. Это ' \
           'очень опасная позиция, и она доставит Вам наприятности, если еще не доставила.'
S_G1_F34 = 'Вы вовсе не являетесь способным или открытым человеком. Вы в действительности не способны открыто ' \
           'встретиться лицом к лицу с другими людьми или ситуациями. Даже несмотря на то, что Вы считаете, что Вы ' \
           'достаточно ответственный и способный стать причиной чего-либо человек, это на самом деле не так. Что-то ' \
           'делает Вас ответственным до некоторой степени, но Вам, как индивидууму, лучше следить за своими ' \
           'действиями, так как в противном случае у Вас возникнут трудности.'
S_H1_I34 = 'Вы не способны быть чутким, так как Вы не можете поставить себя на место другого человека и, ' \
           'следовательно, понять его точку зрения или ситуацию. Из-за этого Вы в действительности не настолько ' \
           'восприимчивы, как Вы считаете сами, так как Вы пытаетесь быть честным в Вашем отношении только ' \
           'поверхностно. Фактически Ваш недостаток понимания - это плохо и Вы только притворяетесь, что видите ' \
           'хорошее.'
S_I1_H34 = 'Вы крайне критичны. Вы устно и мысленно атакуете окружающих Вас людей низким и злобным образом. Вы ' \
           'думаете, что можете видеть их позицию и точку зрения, но на самом деле это только притворство, так как ' \
           'в действительности в других людях и в том, что Вас окружает, Вы видите большей частью только плохое. ' \
           'Вы можете быть достаточно жестким.'
S_A4_B4_C4 = 'Невротик. Прочно застрял в прошлых потерях. Этот синдром часто указывает на то, что человеку в ' \
             'детстве не уделялось достаточно внимания.'
S_A4_E1 = 'Сильно рассеян.'
S_A4_B4_C4_E1 = 'Человек может быть склонен к суициду.'
S_A4_J4 = 'Если остальная часть графика на приемлимом уровне, то это означает, что человек, возможно находится в ' \
          'окружении, тон которого -1.1, где его теальность уничтожается и он не может общаться, потому что это ' \
          'общение будет извращено и использовано против него.'
S_A4_C4_G4_F1 = 'Вспышки гнева, несдержанность.'
S_A1_H4 = 'Педант.'
S_A1_D23 = 'Человек действует, опираясь на стабильные данные, а не на свою уверенность. Это - "интеллектуальное ' \
           'понимание". Большинство студентов будет стараться действовать таким образом в случае, если они сами ' \
           'не полностью владеют данными.'
S_B4_G4_F1 = 'Чувство неполноценности.'
S_B1_D4 = 'Одолевает маник - веселье безумия.'
S_C4_H4 = 'Проблема настоящего времени.'
S_D4_J1 = 'Не может сдержаться. Компульсивен.'
S_D4_G1 = 'Компульсивный экстраверт.'
S_A4_B4_C4_D1_E1_F1_G4_H4_I4_J4 = 'Капризный, безответственный, занят самим собой, извращенное отношение ко всем ' \
                                  'динамикам, потенциально деструктивный.'
S_D4_G4_H4_I4 = 'Не предоставляет бытийность.'
S_E4_F4_J4 = 'У человека может быть гормональная недостаточность и требуется консультация квалифицированного врача.'
S_E4_F4 = 'Если остальная часть графика на приемлемом уровне, то человек возможно принимает наркотики или алкоголь ' \
          'или сильно подавлен.'
S_E1_G4 = 'Недостаток инициативы.'
S_F1_G4_H4 = 'С этим человеком трудно ладить.'
S_I1_J1_B1_F234 = 'Слащавый и приятный.'
S_I1_J4 = 'Задабривание.'
S_A4_C4_D4_H4_I4_J4 = 'Плохие работники.'
S_C_highest = 'Самоконтроль, обусловленный строгим воспитанием, цель которого состояла в ' \
              'том, что человек не должен показывать никаких эмоций или выражать какое-либо мнение.'

S_D_highest = 'Эйфория - использует наилучшим образом ситуации, в которых находится. В жизни ' \
              'этот человек сражается и мало чего добивается. Настоящее общественное полощение позволяет человеку ' \
              'достаточно хорошо скрывать это под маской "со мной все в порядке".'
S_E_above_F = 'Человек делает больше того, что он может комфортно и умело контролировать. В идеале точки D, E и F ' \
              'должны быть расположены по прямой линии (что говорит о том, что человек контролирует свою ' \
              'деятельность умело и уверенно).'
S_F_above_E = 'Не делает того, что может.'
S_I_highest = 'Человек слишком мягкий и доверчивый, "простофиля".'
