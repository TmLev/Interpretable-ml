# coding=utf-8

import dash_core_components as dcc
import dash_html_components as html


def _get_page_header():
    logo = html.Div([
        html.Img(src="assets/images/logo.svg", className="logo")
    ])
    project_name = html.Div([
        html.A(children="Interpretable Machine Learning", href="/", className="project-name")
    ])

    header = html.Header([
        logo,
        project_name,
    ], className="page-header")

    return header


def _get_page_footer():
    footer = html.Footer([
    ], className="page-footer")

    return footer


def _get_article():
    article_header = html.Header([
        html.H1("Interpretable Machine Learning"),
        html.P("В современном мире машинное обучение способно решить целый спектр разнообразных задач:"
               " от предсказания курса доллара"
               " и перевода текста между языками"
               " до распознавания пешеходов беспилотными автобилями."
               " И, казалось бы, всё хорошо – да, работает не всегда идеально, но работает же!"
               " Можно даже не разбираться, почему и как. Или нельзя?"),
    ], className="article-header")

    sections = [
        html.Div([
            html.H3("Одна ошибка – (не) страшно!"),
            html.P([
                "В задачах, где используется хорошо изученная модель или последствия ошибки невелики,"
                " объяснение того или иного предсказания действительно может показаться излишним."
                " Однако, есть задачи, в которых цена – человеческая жизнь или крупная сумма денежных средств."
                " К примеру, ",
                html.A("определение курса лечения больного раком",
                       href="https://www.theverge.com/2018/7/26/17619382/ibms-watson-cancer-ai-healthcare-science",
                       target="_blank"),
                " или ",
                html.A("торги на бирже",
                       href="https://futurism.com/investing-lawsuit-ai-trades-cost-millions",
                       target="_blank"),
                "."

                " В таких случаях становится важным понимать, почему модель приняла конкретное решение."
                " Иногда это может выявить нерассмотренные краевые случаи "
                " (например, если беспилотный автомобиль определяет велосипед по двум колесам,"
                " то что же тогда будет с унициклом?)"
                " или же факт ",
                html.A("половой дискриминации",
                       href="https://www.reuters.com/article/us-amazon-com-jobs-automation-insight/amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-idUSKCN1MK08G",
                       target="_blank"),
                " при приёме на работу.",

                html.Br(),
                " Но при помощи чего можно ",
                html.Em("понять"),
                " модель?",
            ]),
        ], className="content"),

        html.Div([
            html.H3("Интерпретируемость моделей"),
            html.P([
                "Что же это такое? "
                " Строгого математического определения нет, "
                " но многие считают, что это, говоря простым языком, степень того, насколько человек может понять"
                " поведение модели и её логику при принятии того или иного решения."
                " Чем выше интерпретируемость модели, тем проще нам, людям, осознавать, как модель пришла к ответу."
                " Помимо этого, человек – существо любознательное. "
                " Нам хочется понимать, как устроен мир и как он работает. "
                " Когда машинное обучение применяется в исследованиях и дает хорошие результаты,"
                " всё самое интересное остается внутри чёрной коробки."
                " Интерпретируемость моделей позволяет осознать, "
                " что именно послужило причиной того или иного предсказания.",
                html.Br(),
                " Глобально про интерпретируемость моделей можно рассуждать при помощи разных подходов,"
                " мы же выделим два основных группы и обсудим их."
            ]),

            html.H4("Интерпретация, основанная на особенностях модели"),
            html.P(
                "Самый простой способ добиться того, чтобы модель можно было понять"
                " – использовать, как бы парадоксально это не звучало, понятные модели."
                " Наиболее известные интерпретируемые модели – это линейная и логистическая регрессии,"
                " решающие деревья и решающие правила."
            ),
            html.P(
                "Оценить вклад признака `f` у объекта `x` при использовании линейной регрессии"
                " можно, посмотрев на вес признака, "
                " а оценить его вклад – при помощи произведения веса на само значение."
                " Тут могут возникать проблемы: если два признака коррелируют,"
                " то первый может забрать себе всю славу и большой вес,"
                " а второй останется ни с чем или с противоположным знаком."
            ),
            html.P([
                "Неглубокие решающие деревья и небольшие решающие правила очень хорошо воспринимаются людьми "
                "– они чем-то похожи на то, как думает человек, и потому понятны сами по себе и хорошо интерпретируемы"
                " (подробнее можно почитать ",
                html.A("тут", href="https://christophm.github.io/interpretable-ml-book/simple.html",
                       target="_blank"),
                ").",
            ]),
            html.P(
                "Основным плюсом подхода, основанного на особенностях модели, является то,"
                " что самой модели и её архитектуры уже достаточно."
                " Нет необходимости строить гипотезы о её работе и при этом"
                " в некоторых ситуациях простых моделей оказывается вполне достаточно."
            ),
            html.P(
                "Главный же минус виден невооружённым взглядом – данный подход зафиксирован на одной конкретной модели."
                " Если нужно скорректировать модель, тонеобходимо изменить подход к интерпретируемости."
                " При этом на многих реальных данных линейная регрессия или решающее дерево"
                " не смогут сделать ничего толкового."
                " Иногда необходимо воспользоваться бустингом или нейронными сетями,"
                " но при этом хочется хотя бы примерно понимать,"
                " как модели удалось принять правильное решение."
                " С такими желаниями приходится обращаться к подходам из следующей группы.",
            ),

            html.H4("Интерпретация, не зависящая от модели"),
            html.P(
                "Рассмотрим несколько подходов,"
                " которые позволяют объяснять решение сложной модели для конкретного объекта."
                " Главное предположение, в рамках которого применяюися эти подходы, состоит в том, "
                " что сами признаки должны быть интрепретируемы."
                " Например, эмбединг товара или пиксель картинки вряд ли скажут что-либо человеку."
                " Поэтому вне зависимости от того, насколько сложные признаки использует основная модель,"
                " объясняющая должна работать на чем-то упрощенном. Для текстов обычно рассматривают мешок слов с ограничением на количество слов, а для картинок группы похожих пикселей  суперпиксели. Для объекта с признаковым объяснением x будем обозначать за ¯x его интерпретируемое представление"
            )
        ], className="content")


    ]

    article = html.Article([
        article_header,
        *sections,
    ], className="article")

    return article


def get_app_layout():
    layout = html.Div([
        _get_page_header(),
        _get_article(),
        _get_page_footer(),
    ], className="page")

    return layout