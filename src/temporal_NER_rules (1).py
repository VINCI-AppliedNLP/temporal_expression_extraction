from medspacy.ner import TargetRule
import temporal_token_rules

month_num_pat = temporal_token_rules.month_num_pat
day_num_pat = temporal_token_rules.day_num_pat
year_num_pat = temporal_token_rules.year_num_pat  #1999 or 99
month_pat = temporal_token_rules.month_pat # month words pattern
sep_pat = temporal_token_rules.sep_pat # match separator token

month_num_pat_regex = temporal_token_rules.month_num_pat_regex
day_num_pat_regex = temporal_token_rules.day_num_pat_regex
year_num_pat_regex = temporal_token_rules.year_num_pat_regex  #1999 or 99
sep_pat_regex = temporal_token_rules.sep_pat_regex # match seperator as part of string

duration_concepts = ["SECOND", "MINUTE", "HOUR", "TIME", "DAY", "WEEK", "MONTH", "YEAR"]

date_rules = [

    # ================= EXPLICIT CALENDAR DATE
    #'today', '11/12/23'
    TargetRule(literal="calendar date",
               category="DATE",
               pattern=[{'_': {'concept_tag': 'CAL_DATE'}, 'OP': '+'}],
               attributes=None, on_match=None),

    # April, 4, 2015
    TargetRule(literal="calendar date",
               category="DATE",
               pattern=[{'_': {'concept_tag': 'MONTH'}, 'OP': '+'},
                        {'IS_PUNCT': True, 'OP': '*'},
                        {'IS_SPACE': True, 'OP': '*'},
                        {"TEXT": {"REGEX": f"({day_num_pat})"}, 'OP': '+'},
                        {'IS_PUNCT': True, 'OP': '*'},
                        {'IS_SPACE': True, 'OP': '*'},
                        {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '+'}],
               attributes=None, on_match=None),

    # April, 4,2015 (4,2015 as one token)
    TargetRule(literal="calendar date",
               category="DATE",
               pattern=[{'_': {'concept_tag': 'MONTH'}, 'OP': '+'},
                        {'IS_PUNCT': True, 'OP': '*'},
                        {'IS_SPACE': True, 'OP': '*'},
                        {"TEXT": {"REGEX": f"^({day_num_pat_regex})\W({year_num_pat_regex})$"}, 'OP': '+'},
                        ],
               attributes=None, on_match=None),

    # 04, April, 2015" or "April, 2015"
    TargetRule(literal="calendar date",
               category="DATE",
               pattern=[{"TEXT": {"REGEX": f"({day_num_pat})"}, 'OP': '*'},
                        {'IS_PUNCT': True, 'OP': '*'},
                        {'IS_SPACE': True, 'OP': '*'},
                        {'_': {'concept_tag': 'MONTH'}, 'OP': '+'},
                        {'IS_PUNCT': True, 'OP': '*'},
                        {'IS_SPACE': True, 'OP': '*'},
                        {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '+'}],
               attributes=None, on_match=None),

    # 3rd of April, 2015; 3rd April 2015
    TargetRule(literal="calendar date",
               category="DATE",
               pattern=[{'_': {'concept_tag': 'ORDINAL'}, 'OP': '+'},
                        {'_': {'concept_tag': 'OF'}, 'OP': '*'},
                        {'IS_PUNCT': True, 'OP': '*'},
                        {'IS_SPACE': True, 'OP': '*'},
                        {'_': {'concept_tag': 'MONTH'}, 'OP': '+'},
                        {'IS_PUNCT': True, 'OP': '*'},
                        {'IS_SPACE': True, 'OP': '*'},
                        {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '+'}],
               attributes=None, on_match=None),

    # April 3rd, 2015
    TargetRule(literal="calendar date",
               category="DATE",
               pattern=[{'_': {'concept_tag': 'MONTH'}, 'OP': '+'},
                        {'IS_PUNCT': True, 'OP': '*'},
                        {'IS_SPACE': True, 'OP': '*'},
                        {'_': {'concept_tag': 'ORDINAL'}, 'OP': '+'},
                        {'IS_PUNCT': True, 'OP': '*'},
                        {'IS_SPACE': True, 'OP': '*'},
                        {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '+'}],
               attributes=None, on_match=None),

    # "Today is 03-10-1999, 3-10-99"
    TargetRule(literal="calendar date",
               category="DATE",
               pattern=[{"TEXT": {"REGEX": f"({month_num_pat})"}, 'OP': '+'},
                        {"TEXT": "-", 'OP': '+'},
                        {"TEXT": {"REGEX": f"({day_num_pat})"}, 'OP': '+'},
                        {"TEXT": "-", 'OP': '+'},
                        {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '+'},
                        ],
               attributes=None, on_match=None),

    # "Today is 1999-03-10, 99-3-10"
    TargetRule(literal="calendar date",
               category="DATE",
               pattern=[{"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '+'},
                        {"TEXT": "-", 'OP': '+'},
                        {"TEXT": {"REGEX": f"({month_num_pat})"}, 'OP': '+'},
                        {"TEXT": "-", 'OP': '+'},
                        {"TEXT": {"REGEX": f"({day_num_pat})"}, 'OP': '+'},
                        ],
               attributes=None, on_match=None),

    # on 08-27
    TargetRule(literal="calendar date",
               category="DATE",
               pattern=[{'LOWER': 'on', 'OP': '+'},
                        {"TEXT": {"REGEX": f"({month_num_pat})"}, 'OP': '+'},
                        {"TEXT": "-", 'OP': '+'},
                        {"TEXT": {"REGEX": f"({day_num_pat})"}, 'OP': '+'},
                        ],
               attributes=None, on_match=None),


    # "Today is 03-Feb-99" tokens (03, -, feb-99)
    TargetRule(literal="calendar date",
               category="DATE",
               pattern=[{"TEXT": {"REGEX": f"({day_num_pat})"}, 'OP': '+'},
                        {"TEXT": "-", 'OP': '+'},
                        {'LOWER': {'REGEX': f"({month_pat})[-]({year_num_pat_regex})"}},
                        ],
               attributes=None, on_match=None),

    # today is Feb-03-1999" tokens (feb-03, - ,1999)
    TargetRule(literal="calendar date",
               category="DATE",
               pattern=[{'LOWER': {'REGEX': f"({month_pat})[-]({day_num_pat_regex})"}},
                        {"TEXT": "-", 'OP': '+'},
                        {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '+'}
                        ],
               attributes=None, on_match=None),

    # today is 03-feb
    TargetRule(literal="calendar date",
               category="DATE",
               pattern=[{'LOWER': {'REGEX': f"({day_num_pat})"}, 'OP': '+'},
                        {"TEXT": "-", 'OP': '+'},
                        {"LOWER": {"REGEX": f"({month_pat})"}, 'OP': '+'}
                        ],
               attributes=None, on_match=None),

    # today is 99-feb
    TargetRule(literal="calendar date",
               category="DATE",
               pattern=[{'LOWER': {'REGEX': f"({year_num_pat})"}, 'OP': '+'},
                        {"TEXT": "-", 'OP': '+'},
                        {"LOWER": {"REGEX": f"({month_pat})"}, 'OP': '+'}
                        ],
               attributes=None, on_match=None),


    # today is 99-Feb-03" tokens (99. -. Feb-03)
    TargetRule(literal="calendar date",
               category="DATE",
               pattern=[{"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '+'},
                        {"TEXT": "-", 'OP': '+'},
                        {'LOWER': {'REGEX': f"({month_pat})[-]({day_num_pat_regex})"}, 'OP': '+'},
                        ],
               attributes=None, on_match=None),

    # "Today is 03/Feb/99"token o3 ,/, feb/24
    TargetRule(literal="calendar date",
               category="DATE",
               pattern=[{"TEXT": {"REGEX": f"({day_num_pat})"}, 'OP': '+'},
                        {"TEXT": {"REGEX": f"({sep_pat})"}, 'OP': '+'},
                        {"LOWER": {'REGEX': f"({month_pat})({sep_pat_regex})({year_num_pat_regex})"}, 'OP': '+'},
                        ],
               attributes=None, on_match=None
               ),

    # "Today is 1999/Feb/03"
    TargetRule(literal="calendar date",
               category="DATE",
               pattern=[{"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '+'},
                        {"TEXT": {"REGEX": f"({sep_pat})"}, 'OP': '+'},
                        {"LOWER": {'REGEX': f"({month_pat})({sep_pat_regex})({day_num_pat_regex})"}, 'OP': '+'},
                        ],
               attributes=None, on_match=None
               ),

    # "Today is Feb/03/1999"
    TargetRule(literal="calendar date",
               category="DATE",
               pattern=[{"LOWER": {'REGEX': f"({month_pat})({sep_pat_regex})({day_num_pat_regex})"}, 'OP': '+'},
                        {"TEXT": {"REGEX": f"({sep_pat})"}, 'OP': '+'},
                        {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '+'},
                        ],
               attributes=None, on_match=None
               ),

    # ================= INEXPLICIT CALENDAR DATE
    # He losts his home in Jan, 2015 (only month and year but not days)
    TargetRule(literal="calendar date",
               category="DATE",
               pattern=[{'_': {'concept_tag': 'OF'}, 'OP': '!'},
                        # this is to avoid overlapping span like 'the end of june. 2015'
                        {'LOWER':{'IN':["for", "about", "in", "during", "between"]}, 'OP': '!'}, # not for 3 months
                        {"TEXT": {"REGEX": f"({day_num_pat})"}, 'OP': '!'},
                        {'IS_PUNCT': True, 'OP': '*'},
                        {'IS_SPACE': True, 'OP': '*'},
                        {'_': {'concept_tag': 'MONTH'}, 'OP': '+'},
                        {'IS_PUNCT': True, 'OP': '*'},
                        {'IS_SPACE': True, 'OP': '*'},
                        {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '+'}],
               attributes=None, on_match=None),

    # He was admitted on 03, feb.
    TargetRule(literal="calendar date",
               category="DATE",
               pattern=[{'LOWER':{'IN':["for", "about", "in", "during", "between"]}, 'OP': '!'}, # not for 3 months
                        {"TEXT": {"REGEX": f"({day_num_pat})"}, 'OP': '+'},
                        {'IS_PUNCT': True, 'OP': '*'},
                        {'IS_SPACE': True, 'OP': '*'},
                        {'_': {'concept_tag': 'MONTH'}, 'OP': '+'},
                        {'IS_PUNCT': True, 'OP': '*'},
                        {'IS_SPACE': True, 'OP': '*'},
                        {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '!'}],
               attributes=None, on_match=None),

    # feb 03
    TargetRule(literal="calendar date",
               category="DATE",
               pattern=[{'_': {'concept_tag': 'MONTH'}, 'OP': '+'},
                        {'IS_PUNCT': True, 'OP': '*'},
                        {'IS_SPACE': True, 'OP': '*'},
                        {"TEXT": {"REGEX": f"({day_num_pat})"}, 'OP': '+'},
                        {'IS_PUNCT': True, 'OP': '*'},
                        {'IS_SPACE': True, 'OP': '*'},
                        {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '!'}],
               attributes=None, on_match=None),

    # 3rd of April; 3rd, April
    TargetRule(literal="calendar date",
               category="DATE",
               pattern=[{'_': {'concept_tag': 'ORDINAL'}, 'OP': '+'},
                        {'_': {'concept_tag': 'OF'}, 'OP': '*'},
                        {'IS_PUNCT': True, 'OP': '*'},
                        {'IS_SPACE': True, 'OP': '*'},
                        {'_': {'concept_tag': 'MONTH'}, 'OP': '+'},
                        {'IS_PUNCT': True, 'OP': '*'},
                        {'IS_SPACE': True, 'OP': '*'},
                        {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '!'}],
               attributes=None, on_match=None),

    # April 3rd
    TargetRule(literal="calendar date",
               category="DATE",
               pattern=[{'_': {'concept_tag': 'MONTH'}, 'OP': '+'},
                        {'IS_PUNCT': True, 'OP': '*'},
                        {'IS_SPACE': True, 'OP': '*'},
                        {'_': {'concept_tag': 'ORDINAL'}, 'OP': '+'},
                        {'IS_PUNCT': True, 'OP': '*'},
                        {'IS_SPACE': True, 'OP': '*'},
                        {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '!'}],
               attributes=None, on_match=None),

    # (at/until) the end of jan 2015
    TargetRule(literal="calendar date",
               category="DATE",
               pattern=[{'_': {'concept_tag': "DETERMINER"}, 'OP': '+'},
                        {'_': {'concept_tag': 'END'}, 'OP': '+'},
                        {'_': {'concept_tag': 'OF'}, 'OP': '+'},
                        # this is to avoid overlapping span like 'the end of june. 2015'
                        {'IS_PUNCT': True, 'OP': '*'},
                        {'IS_SPACE': True, 'OP': '*'},
                        {'_': {'concept_tag': 'MONTH'}, 'OP': '+'},
                        {'IS_PUNCT': True, 'OP': '*'},
                        {'IS_SPACE': True, 'OP': '*'},
                        {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '*'}],
               attributes=None, on_match=None),

    # at the end of 2015
    TargetRule(literal="calendar date",
               category="DATE",
               pattern=[{'_': {'concept_tag': "DETERMINER"}, 'OP': '+'},
                        {'_': {'concept_tag': 'END'}, 'OP': '+'},
                        {'_': {'concept_tag': 'OF'}, 'OP': '+'},
                        # this is to avoid overlapping span like 'the end of june. 2015'
                        {'IS_PUNCT': True, 'OP': '*'},
                        {'IS_SPACE': True, 'OP': '*'},
                        {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '+'}],
               attributes=None, on_match=None),

    # (in) the beginning of jan 2015
    TargetRule(literal="calendar date",
               category="DATE",
               pattern=[{'_': {'concept_tag': "DETERMINER"}, 'OP': '+'},
                        {'_': {'concept_tag': 'BEGIN'}, 'OP': '+'},
                        {'_': {'concept_tag': 'OF'}, 'OP': '+'},
                        # this is to avoid overlapping span like 'the end of june. 2015'
                        {'IS_PUNCT': True, 'OP': '*'},
                        {'IS_SPACE': True, 'OP': '*'},
                        {'_': {'concept_tag': 'MONTH'}, 'OP': '+'},
                        {'IS_PUNCT': True, 'OP': '*'},
                        {'IS_SPACE': True, 'OP': '*'},
                        {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '*'}],
               attributes=None, on_match=None),

    # at the beginning of 2015
    TargetRule(literal="calendar date",
               category="DATE",
               pattern=[{'_': {'concept_tag': "DETERMINER"}, 'OP': '+'},
                        {'_': {'concept_tag': 'BEGIN'}, 'OP': '+'},
                        {'_': {'concept_tag': 'OF'}, 'OP': '+'},
                        # this is to avoid overlapping span like 'the end of june. 2015'
                        {'IS_PUNCT': True, 'OP': '*'},
                        {'IS_SPACE': True, 'OP': '*'},
                        {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '+'}],
               attributes=None, on_match=None),

    # in 2015
    TargetRule(literal="calendar date",
               category="DATE",
               pattern=[{'_': {'concept_tag': 'IN'}, 'OP': '+'},
                        {'_': {'concept_tag': 'YEAR'}, 'OP': '+'}],
               attributes=None, on_match=None),

    # on-going (on, -, going)
    TargetRule(literal="calendar date",
               category="DATE",
               pattern=[{'_': {'concept_tag': 'ON'}, 'OP': '+'},
                        {'LOWER': "-"},
                        {'LOWER': "going"}],
               attributes=None, on_match=None),

    # the 6th of this month
    TargetRule(literal="calendar date",
               category="DATE",
               pattern=[{'_': {'concept_tag': "DETERMINER"}, 'OP': '*'},
                        {'_': {'concept_tag': "ORDINAL"}, 'OP': '+'},
                        {'LOWER': "of"},
                        {'LOWER': {
                            'IN': ['this', 'the', 'next', 'last', 'past', 'previous', 'coming', 'following']},
                            'OP': '+'},
                        {'_': {'concept_tag': "MONTH"}, 'OP': '+'}
                        ],
               attributes=None, on_match=None),

    # day 1
    TargetRule(literal="calendar date",
                category="DATE",
                pattern=[{'_': {'concept_tag': "DAY"}, 'OP': '+'},
                        {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},],
                attributes=None, on_match=None),

    # day one
    TargetRule(literal="calendar date",
                category="DATE",
                pattern=[{'_': {'concept_tag': "DAY"}, 'OP': '+'},
                        {'_': {'concept_tag': 'NUMBER'}, 'OP': '+'},],
                attributes=None, on_match=None),

    # holidays
    TargetRule(literal="calendar date",
                category="DATE",
                pattern=[{'LOWER': {'IN': ["labor", "memorial", "independent", "thanksgiving", 'christmas', 'president', 'columbus']}, 'OP': '+'},
                        {'LOWER': "day", 'OP': '+'},],
                attributes=None, on_match=None),

    TargetRule(literal="calendar date",
                category="DATE",
                pattern=[{'LOWER': "new", 'OP': '+'},
                        {'LOWER': "year", 'OP': '+'},],
                attributes=None, on_match=None),

    # present time
    TargetRule(literal="calendar date",
                category="DATE",
                pattern=[{'LOWER': "present", 'OP': '+'},
                        {'LOWER': "time", 'OP': '+'},],
                attributes=None, on_match=None),

    # hospitable day
    TargetRule(literal="calendar date",
                category="DATE",
                pattern=[{'LOWER': {'IN': ["hospital", "postoperative", "operation", "op", "operative"]}, 'OP': '+'},
                        {'LOWER': "day", 'OP': '+'},],
                attributes=None, on_match=None),

    # day of life
    TargetRule(literal="calendar date",
                category="DATE",
                pattern=[{'LOWER': "day", 'OP': '+'},
                        {'LOWER': "of", 'OP': '+'},
                         {'LOWER': "life", 'OP': '+'},],
                attributes=None, on_match=None),

]
# ========== vague DATE expression
# 2 or 3 years ago; two years ago
for d in duration_concepts:
    date_rules.extend([

        # the day of (operation)
        TargetRule(literal="calendar date",
                   category="DATE",
                   pattern=[{'LOWER': "the", 'OP': '+'},
                            {'_': {'concept_tag': d}, 'OP': '+'},
                            {'LOWER': "of", 'OP': '+'},],
                   attributes=None, on_match=None),

        # (at) sometime this/next time/day/week...,  past 3 weeks: NOT for 3 weeks
        TargetRule(literal="calendar date",
                   category="DATE",
                   pattern=[{'LOWER':{'IN':["for", "about", "in", "during", "between"]}, 'OP': '!'},
                            {'LOWER': {'IN': ["sometime", "later", "earlier"]}, 'OP': '*'},
                            {'LOWER': "the", 'OP': '*'},
                            {'LOWER': {
                                'IN': ['this', 'the', 'next', 'last', 'past', 'previous', 'coming', 'following']},
                                'OP': '+'},
                            {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '*'},
                            {'_': {'concept_tag': d}, 'OP': '+'}],
                   attributes=None, on_match=None),

        # (at) this/next time/day/week...,  past three weeks
        TargetRule(literal="calendar date",
                   category="DATE",
                   pattern=[{'LOWER':{'IN':["for", "about", "in", "during", "between"]}, 'OP': '!'},
                            {'LOWER': {'IN': ["sometime", "later", "earlier"]}, 'OP': '*'},
                            {'LOWER': "the", 'OP': '*'},
                            {'LOWER': {
                                'IN': ['this', 'the', 'next', 'last', 'past', 'previous', 'coming', 'following']},
                                'OP': '+'},
                            {'_': {'concept_tag': 'NUMBER'}, 'OP': '+'},
                            {'_': {'concept_tag': d}, 'OP': '+'}],
                   attributes=None, on_match=None),

        # until December
        TargetRule(literal="calendar date",
                   category="DATE",
                   pattern=[{'LOWER': {'IN': ["until", "till"]}, 'OP': '+'},
                            {'LOWER': "the", 'OP': '*'},
                            {'LOWER': {
                                'IN': ['this', 'the', 'next', 'last', 'past', 'previous', 'coming', 'following']},
                                'OP': '*'},
                            {'_': {'concept_tag': d}, 'OP': '+'}
                            ],
                   attributes=None, on_match=None),

        # 2 years ago
        TargetRule(literal="vague date",
                   category="DATE",
                   pattern=[{'_': {'concept_tag': "OR"}, 'OP': '!'},
                            {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                            {'_': {'concept_tag': d}, 'OP': '+'},
                            {'_': {'concept_tag': "AGO"}, 'OP': '+'}],
                   attributes=None, on_match=None),
        # two years ago
        TargetRule(literal="vague date",
                   category="DATE",
                   pattern=[{'_': {'concept_tag': "OR"}, 'OP': '!'},
                            {'_': {'concept_tag': 'NUMBER'}, 'OP': '+'},
                            {'_': {'concept_tag': d}, 'OP': '+'},
                            {'_': {'concept_tag': "AGO"}, 'OP': '+'}],
                   attributes=None, on_match=None),
        # 2 or 3 years ago
        TargetRule(literal="vague date",
                   category="DATE",
                   pattern=[{"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                            {'_': {'concept_tag': "OR"}, 'OP': '+'},
                            {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                            {'_': {'concept_tag': d}, 'OP': '+'},
                            {'_': {'concept_tag': "AGO"}, 'OP': '+'}],
                   attributes=None, on_match=None),

        # within 5 days
        TargetRule(literal="vague date",
                   category="DATE",
                   pattern=[{'_': {'concept_tag': "WITHIN"}, 'OP': '+'},
                            {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                            {'_': {'concept_tag': d}, 'OP': '+'}],
                   attributes=None, on_match=None),

        # within five days
        TargetRule(literal="vague date",
                   category="DATE",
                   pattern=[{'_': {'concept_tag': "WITHIN"}, 'OP': '+'},
                            {'_': {'concept_tag': 'NUMBER'}, 'OP': '+'},
                            {'_': {'concept_tag': d}, 'OP': '+'}],
                   attributes=None, on_match=None),

        # at the end of this day
        TargetRule(literal="vague date",
                   category="DATE",
                   pattern=[{'_': {'concept_tag': 'AT'}, 'OP': '*'},
                            {'_': {'concept_tag': 'UNTIL'}, 'OP': '*'},
                            {'_': {'concept_tag': "DETERMINER"}, 'OP': '+'},
                            {'_': {'concept_tag': 'END'}, 'OP': '+'},
                            {'_': {'concept_tag': 'OF'}, 'OP': '+'},
                            # this is to avoid overlapping span like 'the end of june. 2015'
                            {'IS_PUNCT': True, 'OP': '*'},
                            {'IS_SPACE': True, 'OP': '*'},
                            {'_': {'concept_tag': "DETERMINER"}, 'OP': '*'},
                            {'_': {'concept_tag': d}, 'OP': '+'}, ],
                   attributes=None, on_match=None),

        # at the beginnin of this day
        TargetRule(literal="vague date",
                   category="DATE",
                   pattern=[{'_': {'concept_tag': 'AT'}, 'OP': '*'},
                            {'_': {'concept_tag': 'UNTIL'}, 'OP': '*'},
                            {'_': {'concept_tag': "DETERMINER"}, 'OP': '+'},
                            {'_': {'concept_tag': 'BEGIN'}, 'OP': '+'},
                            {'_': {'concept_tag': 'OF'}, 'OP': '+'},
                            # this is to avoid overlapping span like 'the end of june. 2015'
                            {'IS_PUNCT': True, 'OP': '*'},
                            {'IS_SPACE': True, 'OP': '*'},
                            {'_': {'concept_tag': "DETERMINER"}, 'OP': '*'},
                            {'_': {'concept_tag': d}, 'OP': '+'}, ],
                   attributes=None, on_match=None),

        # in this year, in june, in this week ...
        TargetRule(literal="vague date",
                   category="DATE",
                   pattern=[{'_': {'concept_tag': 'IN'}, 'OP': '+'},
                            {'_': {'concept_tag': "DETERMINER"}, 'OP': '*'},
                            {'_': {'concept_tag': d}, 'OP': '+'}, ],
                   attributes=None, on_match=None),
    ])

time_rules = [

    # 9 am, 9am
    TargetRule(literal="time",
               category="TIME",
               pattern=[{"TEXT": {"REGEX": "^(\d|10|11|12)$"}, 'OP': '+'},
                        {'IS_SPACE': True, 'OP': '*'},
                        {'_': {'concept_tag': 'TIME'}, 'OP': '+'}],
               attributes=None, on_match=None),

    # 9:00 am, 09:00am, 23:59
    TargetRule(literal="time",
               category="TIME",
               pattern=[{"TEXT": {"REGEX": "^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$"}, 'OP': '+'},
                        {'IS_SPACE': True, 'OP': '*'},
                        {'_': {'concept_tag': 'TIME'}, 'OP': '*'}],
               attributes=None, on_match=None),

    # 23:59:59, 1:00:00 am
    TargetRule(literal="time",
               category="TIME",
               pattern=[{"TEXT": {"REGEX": "^([0-1]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$"}, 'OP': '+'},
                        {'IS_SPACE': True, 'OP': '*'},
                        {'_': {'concept_tag': 'TIME'}, 'OP': '*'}],
               attributes=None, on_match=None),

    # @9 am, 9am
    TargetRule(literal="time",
               category="TIME",
               pattern=[{"TEXT": {"REGEX": "^\W(\d|10|11|12)$"}, 'OP': '+'}, #match non word charactor like @
                        {'IS_SPACE': True, 'OP': '*'},
                        {'_': {'concept_tag': 'TIME'}, 'OP': '+'}],
               attributes=None, on_match=None),

    # @9:00 am, 09:00am, 23:59
    TargetRule(literal="time",
               category="TIME",
               pattern=[{"TEXT": {"REGEX": "^\W([0-1]?[0-9]|2[0-3]):[0-5][0-9]$"}, 'OP': '+'},
                        {'IS_SPACE': True, 'OP': '*'},
                        {'_': {'concept_tag': 'TIME'}, 'OP': '*'}],
               attributes=None, on_match=None),

    # @23:59:59, 1:00:00 am
    TargetRule(literal="time",
               category="TIME",
               pattern=[{"TEXT": {"REGEX": "^\W([0-1]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$"}, 'OP': '+'},
                        {'IS_SPACE': True, 'OP': '*'},
                        {'_': {'concept_tag': 'TIME'}, 'OP': '*'}],
               attributes=None, on_match=None),

]

duration_rules = []
for d in duration_concepts:
    duration_rules.extend([
        # (at) sometime this/next time/day/week...,  for past 3 weeks
        TargetRule(literal="duration",
                   category="DURATION",
                   pattern=[{'LOWER': {'IN': ["for", "about", "in", "during", "between", "nearly", "almost"]}, 'OP': '+'},
                            {'LOWER': {'IN': ["sometime", "later", "earlier"]}, 'OP': '*'},
                            {'LOWER': "the", 'OP': '*'},
                            {'LOWER': {
                                'IN': ['this', 'the', 'next', 'last', 'past', 'previous', 'coming', 'following']},
                                'OP': '+'},
                            {'LOWER': "of", 'OP':'*'},
                            {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '*'},
                            {'_': {'concept_tag': d}, 'OP': '+'}],
                   attributes=None, on_match=None),

        # a ten day
        TargetRule(literal="duration",
                   category="DURATION",
                   pattern=[
                       {'LOWER': {'IN': ["an", "a"]}, 'OP': '+'},
                       {'_': {'concept_tag': 'NUMBER'}, 'OP': '+'},
                       {'_': {'concept_tag': d}, 'OP': '+'}],
                   attributes=None, on_match=None),

        # a 10 day
        TargetRule(literal="duration",
                   category="DURATION",
                   pattern=[
                       {'LOWER': {'IN': ["an", "a"]}, 'OP': '+'},
                       {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                       {'_': {'concept_tag': d}, 'OP': '+'}],
                   attributes=None, on_match=None),

        # couple of days
        TargetRule(literal="duration",
                   category="DURATION",
                   pattern=[
                       {'LOWER': {'IN':["the", "a"]}, 'OP': '*'},
                       {'LOWER': {
                           'IN': ['this', 'next', 'last', 'past', 'previous', 'coming', 'following']},
                           'OP': '*'},
                       {'LOWER': {'IN': ['few', 'several', 'couple']}, 'OP': '+'},
                       {'LOWER': "of", 'OP': '*'},
                       {'_': {'concept_tag': d}, 'OP': '+'}],
                   attributes=None, on_match=None),

        # (at) this/next time/day/week...,  for past three weeks
        TargetRule(literal="duration",
                   category="DURATION",
                   pattern=[{'LOWER': {'IN': ["for", "about", "in", "during", "between", "nearly", "almost"]}, 'OP': '+'},
                            {'LOWER': {'IN': ["sometime", "later", "earlier"]}, 'OP': '*'},
                            {'LOWER': "the", 'OP': '*'},
                            {'LOWER': {
                                'IN': ['this', 'the', 'next', 'last', 'past', 'previous', 'coming', 'following', 'several', 'couple']},
                                'OP': '+'},
                            {'LOWER': "of", 'OP': '*'},
                            {'_': {'concept_tag': 'NUMBER'}, 'OP': '+'},
                            {'_': {'concept_tag': d}, 'OP': '+'}],
                   attributes=None, on_match=None),

        # 2 days, 2 minutes ...
        TargetRule(literal="duration",
                   category="DURATION",
                   pattern=[{'LOWER': {'IN': ["for", "about", "in", "during", "between", "nearly", "almost"]}, 'OP': '*'},
                            {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                            {'_': {'concept_tag': d}, 'OP': '+'},
                            {'_': {'concept_tag': "AGO"}, 'OP': '!'}],
                   attributes=None, on_match=None),

        # two days, two minutes
        TargetRule(literal="duration",
                   category="DURATION",
                   pattern=[{'LOWER': {'IN': ["for", "about", "in", "during", "between", "nearly", "almost"]}, 'OP': '*'},
                            {'_': {'concept_tag': 'NUMBER'}, 'OP': '+'},
                            {'_': {'concept_tag': d}, 'OP': '+'},
                            {'_': {'concept_tag': "AGO"}, 'OP': '!'}],
                   attributes=None, on_match=None),

        #4 and one half years since
        TargetRule(literal="duration",
                   category="DURATION",
                   pattern=[{'LOWER': {'IN': ["for", "about", "in", "during", "between", "nearly", "almost", "from"]}, 'OP': '*'},
                            {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                            {'LOWER': "and", 'OP': '+'},
                            {'LOWER': "one", 'OP': '+'},
                            {'LOWER': "half", 'OP': '+'},
                            {'_': {'concept_tag': d}, 'OP': '+'},
                            {'_': {'concept_tag': "AGO"}, 'OP': '!'}],
                   attributes=None, on_match=None),

        # 37 5/7 week
        TargetRule(literal="duration",
                   category="DURATION",
                   pattern=[
                       {'LOWER': {'IN': ["for", "about", "in", "during", "between", "nearly", "almost"]}, 'OP': '*'},
                       {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                       {'LOWER': 'and', 'OP':'*'},
                       {"TEXT": {"REGEX": "^[1-9]/[1-9]$"}, 'OP': '+'},
                       {'_': {'concept_tag': d}, 'OP': '+'},
                       {'_': {'concept_tag': "AGO"}, 'OP': '!'}],
                   attributes=None, on_match=None),

        #another week
        TargetRule(literal="duration",
                   category="DURATION",
                   pattern=[{'LOWER': {'IN': ["for", "about", "in", "during", "between", "nearly", "almost", "from"]},
                             'OP': '*'},
                            {'LOWER': "another", 'OP': '+'},
                            {'_': {'concept_tag': d}, 'OP': '+'},
                            {'_': {'concept_tag': "AGO"}, 'OP': '!'}],
                   attributes=None, on_match=None),

        # 1 to 3 days
        TargetRule(literal="duration",
                   category="DURATION",
                   pattern=[{'LOWER': {'IN': ["for", "about", "in", "during", "between", "nearly", "almost", "from"]}, 'OP': '*'},
                            {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                            {'LOWER': "to", 'OP': '+'},
                            {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                            {'_': {'concept_tag': d}, 'OP': '+'},
                            {'_': {'concept_tag': "AGO"}, 'OP': '!'}],
                   attributes=None, on_match=None),

        # one to three days
        TargetRule(literal="duration",
                   category="DURATION",
                   pattern=[{'LOWER': {'IN': ["for", "about", "in", "during", "between", "nearly", "almost", "from"]}, 'OP': '*'},
                            {'_': {'concept_tag': 'NUMBER'}, 'OP': '+'},
                            {'LOWER': "to", 'OP': '+'},
                            {'_': {'concept_tag': 'NUMBER'}, 'OP': '+'},
                            {'_': {'concept_tag': d}, 'OP': '+'},
                            {'_': {'concept_tag': "AGO"}, 'OP': '!'}],
                   attributes=None, on_match=None),

        # 1-3 days
        TargetRule(literal="duration",
                   category="DURATION",
                   pattern=[{'LOWER': {'IN': ["for", "about", "in", "during", "between", "nearly", "almost", "from"]}, 'OP': '*'},
                            {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                            {'LOWER': "-", 'OP': '+'},
                            {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                            {'_': {'concept_tag': d}, 'OP': '+'},
                            {'_': {'concept_tag': "AGO"}, 'OP': '!'}],
                   attributes=None, on_match=None),

        # at least 3 days
        TargetRule(literal="duration",
                   category="DURATION",
                   pattern=[{'LOWER': {'IN': ["for", "about", "in", "during", "between", "nearly", "almost"]}, 'OP': '*'},
                            {'LOWER': "at", 'OP': '+'},
                            {'LOWER': "least", 'OP': '+'},
                            {'LOWER': {'IN': ["for", "about", "in", "during"]}, 'OP': '*'},
                            {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                            {'_': {'concept_tag': d}, 'OP': '+'},
                            {'_': {'concept_tag': "AGO"}, 'OP': '!'}],
                   attributes=None, on_match=None),

        # at least three days
        TargetRule(literal="duration",
                   category="DURATION",
                   pattern=[{'LOWER': {'IN': ["for", "about", "in", "during", "between", "nearly", "almost"]}, 'OP': '*'},
                            {'LOWER': "at", 'OP': '+'},
                            {'LOWER': "least", 'OP': '+'},
                            {'LOWER': {'IN': ["for", "about", "in", "during"]}, 'OP': '*'},
                            {'_': {'concept_tag': 'NUMBER'}, 'OP': '+'},
                            {'_': {'concept_tag': d}, 'OP': '+'},
                            {'_': {'concept_tag': "AGO"}, 'OP': '!'}],
                   attributes=None, on_match=None),

        # more than (less than) 3 days
        TargetRule(literal="duration",
                   category="DURATION",
                   pattern=[{'LOWER': {'IN': ["for", "about", "in", "during", "between", "nearly", "almost"]}, 'OP': '*'},
                            {'LOWER': {'IN': ["more", "less"]}, 'OP': '+'},
                            {'LOWER': "than", 'OP': '+'},
                            {'LOWER': {'IN': ["for", "about", "in", "during"]}, 'OP': '*'},
                            {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                            {'_': {'concept_tag': d}, 'OP': '+'},
                            {'_': {'concept_tag': "AGO"}, 'OP': '!'}],
                   attributes=None, on_match=None),

        # more than three days
        TargetRule(literal="duration",
                   category="DURATION",
                   pattern=[{'LOWER': {'IN': ["for", "about", "in", "during", "between", "nearly", "almost"]}, 'OP': '*'},
                            {'LOWER': {'IN': ["more", "less"]}, 'OP': '+'},
                            {'LOWER': "than", 'OP': '+'},
                            {'LOWER': {'IN': ["for", "about", "in", "during"]}, 'OP': '*'},
                            {'_': {'concept_tag': 'NUMBER'}, 'OP': '+'},
                            {'_': {'concept_tag': d}, 'OP': '+'},
                            {'_': {'concept_tag': "AGO"}, 'OP': '!'}],
                   attributes=None, on_match=None),
    ]
    )
    # DURATION special cases
duration_rules.extend([
        # for january
        TargetRule(literal="duration",
                   category="DURATION",
                   pattern=[{'LOWER': {'IN': ["for", "about", "in", "during", "between", "nearly", "almost"]}, 'OP': '+'},
                            {'_': {'concept_tag': "MONTH"}, 'OP': '+'},
                            {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '!'},
                            {'_': {'concept_tag': "AGO"}, 'OP': '!'}],
                   attributes=None, on_match=None),
        # for 2015
        TargetRule(literal="duration",
                   category="DURATION",
                   pattern=[{'LOWER': {'IN': ["for", "about", "in", "during", "between", "nearly", "almost"]}, 'OP': '+'},
                            {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '+'},
                            {'_': {'concept_tag': "AGO"}, 'OP': '!'}],
                   attributes=None, on_match=None),

        # overnight
        TargetRule(literal="duration",
               category="DURATION",
               pattern=[{'LOWER': "overnight", 'OP': '+'},],
               attributes=None, on_match=None),

    ])

frequency_rules = [

    # weekly, daily, weekly etc.
    TargetRule(literal="frequency",
               category="FREQUENCY",
               pattern=[{'_': {'concept_tag': 'FREQUENCY'}, 'OP': '+'}],
               attributes=None, on_match=None),

    # x 2
    TargetRule(literal="frequency",
               category="FREQUENCY",
               pattern=[{'LOWER': "x", 'OP': '+'},
                        {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                        ],
               attributes=None, on_match=None),
    # x2
    TargetRule(literal="frequency",
               category="FREQUENCY",
               pattern=[
                        {"LOWER": {"REGEX": "^x[0-9]$"}, 'OP': '+'},
                        ],
               attributes=None, on_match=None),

    # every day, every week, every month
    TargetRule(literal="frequency",
               category="FREQUENCY",
               pattern=[{'LOWER': {'IN': ['every', 'each', 'per']}, 'OP': '+'},
                        {'_': {'concept_tag': 'DAY'}, 'OP': '+'}, ],
               attributes=None, on_match=None),

    TargetRule(literal="frequency",
               category="FREQUENCY",
               pattern=[{'LOWER': {'IN': ['every', 'each', 'per']}, 'OP': '+'},
                        {'_': {'concept_tag': 'WEEK'}, 'OP': '+'}, ],
               attributes=None, on_match=None),

    TargetRule(literal="frequency",
               category="FREQUENCY",
               pattern=[{'LOWER': {'IN': ['every', 'each', 'per']}, 'OP': '+'},
                        {'_': {'concept_tag': 'MONTH'}, 'OP': '+'}, ],
               attributes=None, on_match=None),

    TargetRule(literal="frequency",
               category="FREQUENCY",
               pattern=[{'LOWER': {'IN': ['every', 'each', 'per']}, 'OP': '+'},
                        {'_': {'concept_tag': 'YEAR'}, 'OP': '+'}, ],
               attributes=None, on_match=None),

    TargetRule(literal="frequency",
               category="FREQUENCY",
               pattern=[{'LOWER': {'IN': ['every', 'each', 'per']}, 'OP': '+'},
                        {'_': {'concept_tag': 'HOUR'}, 'OP': '+'}, ],
               attributes=None, on_match=None),

    # 2 times every day
    TargetRule(literal="frequency",
               category="FREQUENCY",
               pattern=[{"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                        {'_': {'concept_tag': 'FREQUENCY_UNIT'}, 'OP': '+'},
                        {'_': {'concept_tag': 'DETERMINER'}, 'OP': '+'},
                        {'_': {'concept_tag': 'DAY'}, 'OP': '+'},
                        ],
               attributes=None, on_match=None),

    # 2 times 3 day
    TargetRule(literal="frequency",
               category="FREQUENCY",
               pattern=[{"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '*'},
                        {'_': {'concept_tag': 'FREQUENCY_UNIT'}, 'OP': '+'},
                        {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                        {'_': {'concept_tag': 'DAY'}, 'OP': '+'},
                        ],
               attributes=None, on_match=None),

    # 2 times every week
    TargetRule(literal="frequency",
               category="FREQUENCY",
               pattern=[{"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                        {'_': {'concept_tag': 'FREQUENCY_UNIT'}, 'OP': '+'},
                        {'_': {'concept_tag': 'DETERMINER'}, 'OP': '+'},
                        {'_': {'concept_tag': 'WEEK'}, 'OP': '+'},
                        ],
               attributes=None, on_match=None),

    # 2 times 3 weeks
    TargetRule(literal="frequency",
               category="FREQUENCY",
               pattern=[{"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '*'},
                        {'_': {'concept_tag': 'FREQUENCY_UNIT'}, 'OP': '+'},
                        {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                        {'_': {'concept_tag': 'WEEK'}, 'OP': '+'},
                        ],
               attributes=None, on_match=None),

    # 2 times every month
    TargetRule(literal="frequency",
               category="FREQUENCY",
               pattern=[{"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                        {'_': {'concept_tag': 'FREQUENCY_UNIT'}, 'OP': '+'},
                        {'_': {'concept_tag': 'DETERMINER'}, 'OP': '+'},
                        {'_': {'concept_tag': 'MONTH'}, 'OP': '+'},
                        ],
               attributes=None, on_match=None),

    # 2 times 3 month
    TargetRule(literal="frequency",
               category="FREQUENCY",
               pattern=[{"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '*'},
                        {'_': {'concept_tag': 'FREQUENCY_UNIT'}, 'OP': '+'},
                        {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                        {'_': {'concept_tag': 'MONTH'}, 'OP': '+'},
                        ],
               attributes=None, on_match=None),

    # 2 times every year
    TargetRule(literal="frequency",
               category="FREQUENCY",
               pattern=[{"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                        {'_': {'concept_tag': 'FREQUENCY_UNIT'}, 'OP': '+'},
                        {'_': {'concept_tag': 'DETERMINER'}, 'OP': '+'},
                        {'_': {'concept_tag': 'YEAR'}, 'OP': '+'},
                        ],
               attributes=None, on_match=None),

    # 2 times 3 year
    TargetRule(literal="frequency",
               category="FREQUENCY",
               pattern=[{"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '*'},
                        {'_': {'concept_tag': 'FREQUENCY_UNIT'}, 'OP': '+'},
                        {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                        {'_': {'concept_tag': 'YEAR'}, 'OP': '+'},
                        ],
               attributes=None, on_match=None),

    # 2 times every hour
    TargetRule(literal="frequency",
               category="FREQUENCY",
               pattern=[{"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                        {'_': {'concept_tag': 'FREQUENCY_UNIT'}, 'OP': '+'},
                        {'_': {'concept_tag': 'DETERMINER'}, 'OP': '+'},
                        {'_': {'concept_tag': 'HOUR'}, 'OP': '+'},
                        ],
               attributes=None, on_match=None),

    # 2 times 3 hour
    TargetRule(literal="frequency",
               category="FREQUENCY",
               pattern=[{"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '*'},
                        {'_': {'concept_tag': 'FREQUENCY_UNIT'}, 'OP': '+'},
                        {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                        {'_': {'concept_tag': 'HOUR'}, 'OP': '+'},
                        ],
               attributes=None, on_match=None),


    # two times a week
    TargetRule(literal="frequency",
               category="FREQUENCY",
               pattern=[{'_': {'concept_tag': 'NUMBER'}, 'OP': '+'},
                        {'_': {'concept_tag': 'FREQUENCY_UNIT'}, 'OP': '+'},
                        {'_': {'concept_tag': 'DETERMINER'}, 'OP': '+'},
                        {'_': {'concept_tag': 'DAY'}, 'OP': '+'},
                        ],
               attributes=None, on_match=None),

    TargetRule(literal="frequency",
               category="FREQUENCY",
               pattern=[{'_': {'concept_tag': 'NUMBER'}, 'OP': '*'},
                        {'_': {'concept_tag': 'FREQUENCY_UNIT'}, 'OP': '+'},
                        {'_': {'concept_tag': 'NUMBER'}, 'OP': '+'},
                        {'_': {'concept_tag': 'DAY'}, 'OP': '+'},
                        ],
               attributes=None, on_match=None),

    TargetRule(literal="frequency",
               category="FREQUENCY",
               pattern=[{'_': {'concept_tag': 'NUMBER'}, 'OP': '+'},
                        {'_': {'concept_tag': 'FREQUENCY_UNIT'}, 'OP': '+'},
                        {'_': {'concept_tag': 'DETERMINER'}, 'OP': '+'},
                        {'_': {'concept_tag': 'WEEK'}, 'OP': '+'},
                        ],
               attributes=None, on_match=None),

    TargetRule(literal="frequency",
               category="FREQUENCY",
               pattern=[{'_': {'concept_tag': 'NUMBER'}, 'OP': '*'},
                        {'_': {'concept_tag': 'FREQUENCY_UNIT'}, 'OP': '+'},
                        {'_': {'concept_tag': 'NUMBER'}, 'OP': '+'},
                        {'_': {'concept_tag': 'WEEK'}, 'OP': '+'},
                        ],
               attributes=None, on_match=None),

    TargetRule(literal="frequency",
               category="FREQUENCY",
               pattern=[{'_': {'concept_tag': 'NUMBER'}, 'OP': '+'},
                        {'_': {'concept_tag': 'FREQUENCY_UNIT'}, 'OP': '+'},
                        {'_': {'concept_tag': 'DETERMINER'}, 'OP': '+'},
                        {'_': {'concept_tag': 'MONTH'}, 'OP': '+'},
                        ],
               attributes=None, on_match=None),

    TargetRule(literal="frequency",
               category="FREQUENCY",
               pattern=[{'_': {'concept_tag': 'NUMBER'}, 'OP': '*'},
                        {'_': {'concept_tag': 'FREQUENCY_UNIT'}, 'OP': '+'},
                        {'_': {'concept_tag': 'NUMBER'}, 'OP': '+'},
                        {'_': {'concept_tag': 'MONTH'}, 'OP': '+'},
                        ],
               attributes=None, on_match=None),

    TargetRule(literal="frequency",
               category="FREQUENCY",
               pattern=[{'_': {'concept_tag': 'NUMBER'}, 'OP': '+'},
                        {'_': {'concept_tag': 'FREQUENCY_UNIT'}, 'OP': '+'},
                        {'_': {'concept_tag': 'DETERMINER'}, 'OP': '+'},
                        {'_': {'concept_tag': 'YEAR'}, 'OP': '+'},
                        ],
               attributes=None, on_match=None),

    TargetRule(literal="frequency",
               category="FREQUENCY",
               pattern=[{'_': {'concept_tag': 'NUMBER'}, 'OP': '*'},
                        {'_': {'concept_tag': 'FREQUENCY_UNIT'}, 'OP': '+'},
                        {'_': {'concept_tag': 'NUMBER'}, 'OP': '+'},
                        {'_': {'concept_tag': 'YEAR'}, 'OP': '+'},
                        ],
               attributes=None, on_match=None),

    TargetRule(literal="frequency",
               category="FREQUENCY",
               pattern=[{'_': {'concept_tag': 'NUMBER'}, 'OP': '+'},
                        {'_': {'concept_tag': 'FREQUENCY_UNIT'}, 'OP': '+'},
                        {'_': {'concept_tag': 'DETERMINER'}, 'OP': '+'},
                        {'_': {'concept_tag': 'HOUR'}, 'OP': '+'},
                        ],
               attributes=None, on_match=None),

    TargetRule(literal="frequency",
               category="FREQUENCY",
               pattern=[{'_': {'concept_tag': 'NUMBER'}, 'OP': '*'},
                        {'_': {'concept_tag': 'FREQUENCY_UNIT'}, 'OP': '+'},
                        {'_': {'concept_tag': 'NUMBER'}, 'OP': '+'},
                        {'_': {'concept_tag': 'HOUR'}, 'OP': '+'},
                        ],
               attributes=None, on_match=None),

]

quantifier_rules = [
    # 2 times, 2 episodes NOT 2 times every week
    TargetRule(literal="quantifier",
               category="QUANTIFIER",
               pattern=[{"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                        {'_': {'concept_tag': 'FREQUENCY_UNIT'}, 'OP': '+'},
                        {'LOWER': "of", 'OP':'+'},
                        #{'_': {'concept_tag': 'DETERMINER'}, 'OP': '!'}
                        ],
               attributes=None, on_match=None),

    # two times, NOT two times every week
    TargetRule(literal="quantifier",
               category="QUANTIFIER",
               pattern=[{'_': {'concept_tag': 'NUMBER'}, 'OP': '+'},
                        {'_': {'concept_tag': 'FREQUENCY_UNIT'}, 'OP': '+'},
                        {'LOWER': "of", 'OP':'+'},
                        {'_': {'concept_tag': 'DETERMINER'}, 'OP': '!'}],
               attributes=None, on_match=None),

]


def get_NER_rules():
    return date_rules + duration_rules #+ time_rules + frequency_rules + quantifier_rules
