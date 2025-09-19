import temporal_token_rules

month_num_pat = temporal_token_rules.month_num_pat
day_num_pat = temporal_token_rules.day_num_pat
year_num_pat = temporal_token_rules.year_num_pat  #1999 or 99
month_pat = temporal_token_rules.month_pat  # month words pattern
sep_pat = temporal_token_rules.sep_pat  # match separator token

month_num_pat_regex = temporal_token_rules.month_num_pat_regex
day_num_pat_regex = temporal_token_rules.day_num_pat_regex
year_num_pat_regex = temporal_token_rules.year_num_pat_regex  #1999 or 99
sep_pat_regex = temporal_token_rules.sep_pat_regex  # match seperator as part of string

duration_concepts = ["SECOND", "MINUTE", "HOUR", "TIME", "DAY", "WEEK", "MONTH", "YEAR"]

exact_cal_date = [
    # April, 4, 2015
    [{'_': {'concept_tag': 'MONTH'}, 'OP': '+'},
     {'IS_PUNCT': True, 'OP': '*'},
     {'IS_SPACE': True, 'OP': '*'},
     {"TEXT": {"REGEX": f"({day_num_pat})"}, 'OP': '+'},
     {'IS_PUNCT': True, 'OP': '*'},
     {'IS_SPACE': True, 'OP': '*'},
     {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '+'}],

    # April, 4,2015 (4,2015 as one token)
    [{'_': {'concept_tag': 'MONTH'}, 'OP': '+'},
     {'IS_PUNCT': True, 'OP': '*'},
     {'IS_SPACE': True, 'OP': '*'},
     {"TEXT": {"REGEX": f"^({day_num_pat_regex})\W({year_num_pat_regex})$"}, 'OP': '+'},
     ],

    # 04, April, 2015" or "April, 2015"
    [{"TEXT": {"REGEX": f"({day_num_pat})"}, 'OP': '*'},
     {'IS_PUNCT': True, 'OP': '*'},
     {'IS_SPACE': True, 'OP': '*'},
     {'_': {'concept_tag': 'MONTH'}, 'OP': '+'},
     {'IS_PUNCT': True, 'OP': '*'},
     {'IS_SPACE': True, 'OP': '*'},
     {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '+'}],

    # 3rd of April, 2015; 3rd April 2015
    [{'_': {'concept_tag': 'ORDINAL'}, 'OP': '+'},
     {'_': {'concept_tag': 'OF'}, 'OP': '*'},
     {'IS_PUNCT': True, 'OP': '*'},
     {'IS_SPACE': True, 'OP': '*'},
     {'_': {'concept_tag': 'MONTH'}, 'OP': '+'},
     {'IS_PUNCT': True, 'OP': '*'},
     {'IS_SPACE': True, 'OP': '*'},
     {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '+'}],

    # April 3rd, 2015
    [{'_': {'concept_tag': 'MONTH'}, 'OP': '+'},
     {'IS_PUNCT': True, 'OP': '*'},
     {'IS_SPACE': True, 'OP': '*'},
     {'_': {'concept_tag': 'ORDINAL'}, 'OP': '+'},
     {'IS_PUNCT': True, 'OP': '*'},
     {'IS_SPACE': True, 'OP': '*'},
     {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '+'}],

    # "Today is 03-10-1999, 3-10-99"
    [{"TEXT": {"REGEX": f"({month_num_pat})"}, 'OP': '+'},
     {"TEXT": "-", 'OP': '+'},
     {"TEXT": {"REGEX": f"({day_num_pat})"}, 'OP': '+'},
     {"TEXT": "-", 'OP': '+'},
     {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '+'},
     ],

    # "Today is 1999-03-10, 99-3-10"
    [{"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '+'},
     {"TEXT": "-", 'OP': '+'},
     {"TEXT": {"REGEX": f"({month_num_pat})"}, 'OP': '+'},
     {"TEXT": "-", 'OP': '+'},
     {"TEXT": {"REGEX": f"({day_num_pat})"}, 'OP': '+'},
     ],

    # on 08-27
    [{'LOWER': 'on', 'OP': '+'},
     {"TEXT": {"REGEX": f"({month_num_pat})"}, 'OP': '+'},
     {"TEXT": "-", 'OP': '+'},
     {"TEXT": {"REGEX": f"({day_num_pat})"}, 'OP': '+'},
     ],

    # "Today is 03-Feb-99" tokens (03, -, feb-99)
    [{"TEXT": {"REGEX": f"({day_num_pat})"}, 'OP': '+'},
     {"TEXT": "-", 'OP': '+'},
     {'LOWER': {'REGEX': f"({month_pat})[-]({year_num_pat_regex})"}},
     ],

    # today is Feb-03-1999" tokens (feb-03, - ,1999)
    [{'LOWER': {'REGEX': f"({month_pat})[-]({day_num_pat_regex})"}},
     {"TEXT": "-", 'OP': '+'},
     {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '+'}
     ],

    # today is 03-feb
    [{'LOWER': {'REGEX': f"({day_num_pat})"}, 'OP': '+'},
     {"TEXT": "-", 'OP': '+'},
     {"LOWER": {"REGEX": f"({month_pat})"}, 'OP': '+'}
     ],

    # today is 99-feb
    [{'LOWER': {'REGEX': f"({year_num_pat})"}, 'OP': '+'},
     {"TEXT": "-", 'OP': '+'},
     {"LOWER": {"REGEX": f"({month_pat})"}, 'OP': '+'}
     ],
    # today is 99-Feb-03" tokens (99. -. Feb-03)
    [{"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '+'},
     {"TEXT": "-", 'OP': '+'},
     {'LOWER': {'REGEX': f"({month_pat})[-]({day_num_pat_regex})"}, 'OP': '+'},
     ],

    # "Today is 03/Feb/99"token o3 ,/, feb/24
    [{"TEXT": {"REGEX": f"({day_num_pat})"}, 'OP': '+'},
     {"TEXT": {"REGEX": f"({sep_pat})"}, 'OP': '+'},
     {"LOWER": {'REGEX': f"({month_pat})({sep_pat_regex})({year_num_pat_regex})"}, 'OP': '+'},
     ],

    # "Today is 1999/Feb/03"
    [{"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '+'},
     {"TEXT": {"REGEX": f"({sep_pat})"}, 'OP': '+'},
     {"LOWER": {'REGEX': f"({month_pat})({sep_pat_regex})({day_num_pat_regex})"}, 'OP': '+'},
     ],

    # "Today is Feb/03/1999"
    [{"LOWER": {'REGEX': f"({month_pat})({sep_pat_regex})({day_num_pat_regex})"}, 'OP': '+'},
     {"TEXT": {"REGEX": f"({sep_pat})"}, 'OP': '+'},
     {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '+'},
     ],

    # He was admitted on 03, feb.
    [{'LOWER': {'IN': ["for", "about", "in", "during", "between"]}, 'OP': '!'},  # not for 3 months
     {"TEXT": {"REGEX": f"({day_num_pat})"}, 'OP': '+'},
     {'IS_PUNCT': True, 'OP': '*'},
     {'IS_SPACE': True, 'OP': '*'},
     {'_': {'concept_tag': 'MONTH'}, 'OP': '+'},
     {'IS_PUNCT': True, 'OP': '*'},
     {'IS_SPACE': True, 'OP': '*'},
     {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '!'}],

    # feb 03
    [{'_': {'concept_tag': 'MONTH'}, 'OP': '+'},
     {'IS_PUNCT': True, 'OP': '*'},
     {'IS_SPACE': True, 'OP': '*'},
     {"TEXT": {"REGEX": f"({day_num_pat})"}, 'OP': '+'},
     {'IS_PUNCT': True, 'OP': '*'},
     {'IS_SPACE': True, 'OP': '*'},
     {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '!'}],
    # 3rd of April; 3rd, April
    [{'_': {'concept_tag': 'ORDINAL'}, 'OP': '+'},
     {'_': {'concept_tag': 'OF'}, 'OP': '*'},
     {'IS_PUNCT': True, 'OP': '*'},
     {'IS_SPACE': True, 'OP': '*'},
     {'_': {'concept_tag': 'MONTH'}, 'OP': '+'},
     {'IS_PUNCT': True, 'OP': '*'},
     {'IS_SPACE': True, 'OP': '*'},
     {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '!'}],
    # April 3rd
    [{'_': {'concept_tag': 'MONTH'}, 'OP': '+'},
     {'IS_PUNCT': True, 'OP': '*'},
     {'IS_SPACE': True, 'OP': '*'},
     {'_': {'concept_tag': 'ORDINAL'}, 'OP': '+'},
     {'IS_PUNCT': True, 'OP': '*'},
     {'IS_SPACE': True, 'OP': '*'},
     {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '!'}],

    # the 6th of this month
    [{'_': {'concept_tag': "DETERMINER"}, 'OP': '*'},
     {'_': {'concept_tag': "ORDINAL"}, 'OP': '+'},
     {'LOWER': "of"},
     {'LOWER': {
         'IN': ['this', 'the', 'next', 'last', 'past', 'previous', 'coming', 'following']},
         'OP': '+'},
     {'_': {'concept_tag': "MONTH"}, 'OP': '+'}
     ],

    # holidays
    [{'LOWER': {'IN': ["labor", "memorial", "independent", "thanksgiving", 'christmas', 'president', 'columbus']},
      'OP': '+'},
     {'LOWER': "day", 'OP': '+'}, ],

    [{'LOWER': "new", 'OP': '+'},
     {'LOWER': "year", 'OP': '+'}, ],

]

for d in duration_concepts:
    exact_cal_date.extend([
        # 2 years ago
        [{'_': {'concept_tag': "OR"}, 'OP': '!'},
         {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
         {'_': {'concept_tag': d}, 'OP': '+'},
         {'_': {'concept_tag': "AGO"}, 'OP': '+'}],

        # two years ago
        [{'_': {'concept_tag': "OR"}, 'OP': '!'},
         {'_': {'concept_tag': 'NUMBER'}, 'OP': '+'},
         {'_': {'concept_tag': d}, 'OP': '+'},
         {'_': {'concept_tag': "AGO"}, 'OP': '+'}],

        # 2 or 3 years ago
        [{"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
         {'_': {'concept_tag': "OR"}, 'OP': '+'},
         {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
         {'_': {'concept_tag': d}, 'OP': '+'},
         {'_': {'concept_tag': "AGO"}, 'OP': '+'}],

        # within 5 days
        [{'_': {'concept_tag': "WITHIN"}, 'OP': '+'},
         {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
         {'_': {'concept_tag': d}, 'OP': '+'}],

        # within five days
        [{'_': {'concept_tag': "WITHIN"}, 'OP': '+'},
         {'_': {'concept_tag': 'NUMBER'}, 'OP': '+'},
         {'_': {'concept_tag': d}, 'OP': '+'}],

        # at the end of this day
        [{'_': {'concept_tag': 'AT'}, 'OP': '*'},
         {'_': {'concept_tag': 'UNTIL'}, 'OP': '*'},
         {'_': {'concept_tag': "DETERMINER"}, 'OP': '+'},
         {'_': {'concept_tag': 'END'}, 'OP': '+'},
         {'_': {'concept_tag': 'OF'}, 'OP': '+'},
         # this is to avoid overlapping span like 'the end of june. 2015'
         {'IS_PUNCT': True, 'OP': '*'},
         {'IS_SPACE': True, 'OP': '*'},
         {'_': {'concept_tag': "DETERMINER"}, 'OP': '*'},
         {'_': {'concept_tag': d}, 'OP': '+'}, ],

        # at the beginnin of this day
        [{'_': {'concept_tag': 'AT'}, 'OP': '*'},
         {'_': {'concept_tag': 'UNTIL'}, 'OP': '*'},
         {'_': {'concept_tag': "DETERMINER"}, 'OP': '+'},
         {'_': {'concept_tag': 'BEGIN'}, 'OP': '+'},
         {'_': {'concept_tag': 'OF'}, 'OP': '+'},
         # this is to avoid overlapping span like 'the end of june. 2015'
         {'IS_PUNCT': True, 'OP': '*'},
         {'IS_SPACE': True, 'OP': '*'},
         {'_': {'concept_tag': "DETERMINER"}, 'OP': '*'},
         {'_': {'concept_tag': d}, 'OP': '+'}, ],
    ])

    def get_rules():
        return exact_cal_date
