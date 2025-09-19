from medspacy.context import ConTextRule, ConText

import temporal_token_rules
import patterns

allowed_concept_labels = {
    'DOUBLING_UP',
    'EVIDENCE_OF_HOMELESSNESS',
    'EVIDENCE_OF_HOUSING',
    'INSTITUTIONAL',
    'RISK_OF_HOMELESSNESS',
    'SHELTERED_HOMELESSNESS',
    'TEMPORARY_HOUSING',
    'UNSHELTERED_HOMELESSNESS',
    'VA_HOUSING',
}

maxScope = 30  #the maximum tokens the context will search; contrained also my the sentence

month_num_pat = temporal_token_rules.month_num_pat
day_num_pat = temporal_token_rules.day_num_pat
year_num_pat = temporal_token_rules.year_num_pat  #1999 or 99
month_pat = temporal_token_rules.month_pat  # month words pattern
sep_pat = temporal_token_rules.sep_pat  # match separator token

month_num_pat_regex = temporal_token_rules.month_num_pat_regex
day_num_pat_regex = temporal_token_rules.day_num_pat_regex
year_num_pat_regex = temporal_token_rules.year_num_pat_regex  #1999 or 99
sep_pat_regex = temporal_token_rules.sep_pat_regex  # match seperator as part of string

duration_concepts = [ "DAY", "WEEK", "MONTH", "YEAR"]#["SECOND", "MINUTE", "HOUR", "TIME", "DAY", "WEEK", "MONTH", "YEAR"]

overlap_rules = []
contain_rules = []
begin_rules = []
end_rules = []

# all calendar date as OVERLAP, no pattern needed for this set of words
cal_date = ["today", "tonight", "night", "morning", "evening", "afternoon", "tomorrow", "yesterday"]
cal_date_implicit = ["current", "currently", "now", "recent", "recently", "future", "present", "still"]
for c in cal_date:
    overlap_rules.extend([
        ConTextRule(literal=c, category="OVERLAP", direction="BIDIRECTIONAL", max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DATE'})
    ])

for ci in cal_date_implicit:
    contain_rules.extend([
        ConTextRule(literal=ci, category="CONTAINS", direction="BIDIRECTIONAL", max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DATE'})
    ])

# calendar date with prep.
for sep in ['\\.', '/', '\\\\']:  # 3 types of separators
    overlap_rules.extend([
        ConTextRule(literal="calendar date",
                    category="OVERLAP",
                    direction="BIDIRECTIONAL",
                    pattern=[
                        {'LOWER': {'IN': ["on", "at", "of"]}, 'OP': '+'},
                        {'LOWER': {
                            'REGEX': f"({day_num_pat_regex})({sep})({month_num_pat_regex})({sep})({year_num_pat_regex})"},
                            'OP': '+'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DATE'}
                    ),
        ConTextRule(literal="calendar date",
                    category="OVERLAP",
                    direction="BIDIRECTIONAL",
                    pattern=[
                        {'LOWER': {'IN': ["on", "at", "of"]}, 'OP': '+'},
                        {'LOWER': {
                            'REGEX': f"({month_num_pat_regex})({sep})({day_num_pat_regex})({sep})({year_num_pat_regex})"},
                            'OP': '+'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DATE'}
                    ),
        ConTextRule(literal="calendar date",
                    category="OVERLAP",
                    direction="BIDIRECTIONAL",
                    pattern=[
                        {'LOWER': {'IN': ["on", "at", "of"]}, 'OP': '+'},
                        {'LOWER': {
                            'REGEX': f"({year_num_pat_regex})({sep})({month_num_pat_regex})({sep})({day_num_pat_regex})"},
                            'OP': '+'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DATE'}
                    ),
        ConTextRule(literal="calendar date",
                    category="OVERLAP",
                    direction="BIDIRECTIONAL",
                    pattern=[
                        {'LOWER': {'IN': ["on", "at", "of"]}, 'OP': '+'},
                        {'LOWER': {
                            'REGEX': f"({year_num_pat_regex})({sep})({day_num_pat_regex})({sep})({month_num_pat_regex})"},
                            'OP': '+'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DATE'}
                    ),

    ])
    begin_rules.extend([
        ConTextRule(literal="calendar date",
                    category="BEGINS_ON",
                    direction="BIDIRECTIONAL",
                    pattern=[
                        {'LOWER': {'IN': ["from", "since"]}, 'OP': '+'},
                        {'LOWER': {
                            'REGEX': f"({day_num_pat_regex})({sep})({month_num_pat_regex})({sep})({year_num_pat_regex})"},
                            'OP': '+'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DATE'}
                    ),
        ConTextRule(literal="calendar date",
                    category="BEGINS_ON",
                    direction="BIDIRECTIONAL",
                    pattern=[
                        {'LOWER': {'IN': ["from", "since"]}, 'OP': '+'},
                        {'LOWER': {
                            'REGEX': f"({month_num_pat_regex})({sep})({day_num_pat_regex})({sep})({year_num_pat_regex})"},
                            'OP': '+'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DATE'}
                    ),
        ConTextRule(literal="calendar date",
                    category="BEGINS_ON",
                    direction="BIDIRECTIONAL",
                    pattern=[
                        {'LOWER': {'IN': ["from", "since"]}, 'OP': '+'},
                        {'LOWER': {
                            'REGEX': f"({year_num_pat_regex})({sep})({month_num_pat_regex})({sep})({day_num_pat_regex})"},
                            'OP': '+'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DATE'}
                    ),
        ConTextRule(literal="calendar date",
                    category="BEGINS_ON",
                    direction="BIDIRECTIONAL",
                    pattern=[
                        {'LOWER': {'IN': ["from", "since"]}, 'OP': '+'},
                        {'LOWER': {
                            'REGEX': f"({year_num_pat_regex})({sep})({day_num_pat_regex})({sep})({month_num_pat_regex})"},
                            'OP': '+'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DATE'}
                    ),

    ])
    end_rules.extend([
        ConTextRule(literal="calendar date",
                    category="ENDS_ON",
                    direction="BIDIRECTIONAL",
                    pattern=[
                        {'LOWER': {'IN': ["to", "till", "until"]}, 'OP': '+'},
                        {'LOWER': {
                            'REGEX': f"({day_num_pat_regex})({sep})({month_num_pat_regex})({sep})({year_num_pat_regex})"},
                            'OP': '+'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DATE'}
                    ),
        ConTextRule(literal="calendar date",
                    category="ENDS_ON",
                    direction="BIDIRECTIONAL",
                    pattern=[
                        {'LOWER': {'IN': ["to", "till", "until"]}, 'OP': '+'},
                        {'LOWER': {
                            'REGEX': f"({month_num_pat_regex})({sep})({day_num_pat_regex})({sep})({year_num_pat_regex})"},
                            'OP': '+'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DATE'}
                    ),
        ConTextRule(literal="calendar date",
                    category="ENDS_ON",
                    direction="BIDIRECTIONAL",
                    pattern=[
                        {'LOWER': {'IN': ["to", "till", "until"]}, 'OP': '+'},
                        {'LOWER': {
                            'REGEX': f"({year_num_pat_regex})({sep})({month_num_pat_regex})({sep})({day_num_pat_regex})"},
                            'OP': '+'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DATE'}
                    ),
        ConTextRule(literal="calendar date",
                    category="ENDS_ON",
                    direction="BIDIRECTIONAL",
                    pattern=[
                        {'LOWER': {'IN': ["to", "till", "until"]}, 'OP': '+'},
                        {'LOWER': {
                            'REGEX': f"({year_num_pat_regex})({sep})({day_num_pat_regex})({sep})({month_num_pat_regex})"},
                            'OP': '+'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DATE'}
                    ),

    ])
# implicit cal date like 05/16
overlap_rules.extend([
    ConTextRule(literal="calendar date",
                category="OVERLAP",
                direction="BIDIRECTIONAL",
                pattern=[
                    {'LOWER': {'IN': ["on", "at", "of"]}, 'OP': '+'},
                    {'LOWER': {
                        'REGEX': f"^({month_num_pat_regex})(/|\\\\)({day_num_pat_regex})$"}, 'OP': '+'}],
                max_scope=maxScope,
                allowed_types=allowed_concept_labels, metadata={'NER': 'DATE'}
                ),
])
contain_rules.extend([
    ConTextRule(literal="calendar date",
                category="CONTAINS",
                direction="BIDIRECTIONAL",
                pattern=[
                    {'LOWER': {'IN': ["since"]}, 'OP': '+'},
                    {'LOWER': {
                        'REGEX': f"^({month_num_pat_regex})(/|\\\\)({day_num_pat_regex})$"},
                        'OP': '+'}],
                max_scope=maxScope,
                allowed_types=allowed_concept_labels, metadata={'NER': 'DATE'}
                ),
])
begin_rules.extend([
    ConTextRule(literal="calendar date",
                category="BEGINS_ON",
                direction="BIDIRECTIONAL",
                pattern=[
                    {'LOWER': {'IN': ["from", "since"]}, 'OP': '+'},
                    {'LOWER': {
                        'REGEX': f"^({month_num_pat_regex})(/|\\\\)({day_num_pat_regex})$"},
                        'OP': '+'}],
                max_scope=maxScope,
                allowed_types=allowed_concept_labels, metadata={'NER': 'DATE'}
                ),

])
end_rules.extend([
    ConTextRule(literal="calendar date",
                category="ENDS_ON",
                direction="BIDIRECTIONAL",
                pattern=[
                    {'LOWER': {'IN': ["to", "till", "until"]}, 'OP': '+'},
                    {'LOWER': {
                        'REGEX': f"^({month_num_pat_regex})(/|\\\\)({day_num_pat_regex})$"},
                        'OP': '+'}],
                max_scope=maxScope,
                allowed_types=allowed_concept_labels, metadata={'NER': 'DATE'}
                ),

])
# implicit cal date like June-19
for m in temporal_token_rules.month_token:
    contain_rules.extend([
        ConTextRule(literal="calendar date",
                    category="CONTAINS",
                    direction="BIDIRECTIONAL",
                    pattern=[
                        {'LOWER': {'IN': ["since", "in", "within", "during"]}, 'OP': '+'},
                        {'LOWER': {
                            'REGEX': f"^({m})(-)({year_num_pat_regex})$"},
                            'OP': '+'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DURATION'}
                    ),
    ])
    overlap_rules.extend([
        ConTextRule(literal="calendar date",
                    category="OVERLAP",
                    direction="BIDIRECTIONAL",
                    pattern=[
                        {'LOWER': {'IN': ["on", "at", "of"]}, 'OP': '+'},
                        {'LOWER': {
                            'REGEX': f"^({m})(-)({day_num_pat_regex})$"}, 'OP': '+'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DURATION'}
                    ),
    ])
    begin_rules.extend([
        ConTextRule(literal="calendar date",
                    category="BEGINS_ON",
                    direction="BIDIRECTIONAL",
                    pattern=[
                        {'LOWER': {'IN': ["from", "since"]}, 'OP': '+'},
                        {'LOWER': {
                            'REGEX': f"^({m})(-)({day_num_pat_regex})$"},
                            'OP': '+'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DURATION'}
                    ),
        ConTextRule(literal="calendar date",
                    category="BEGINS_ON",
                    direction="BIDIRECTIONAL",
                    pattern=[
                        {'LOWER': {'IN': ["from"]}, 'OP': '+'},
                        {'LOWER': {
                            'REGEX': f"^({m})(-)({year_num_pat_regex})$"},
                            'OP': '+'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DURATION'}
                    ),

    ])
    end_rules.extend([
        ConTextRule(literal="calendar date",
                    category="ENDS_ON",
                    direction="BIDIRECTIONAL",
                    pattern=[
                        {'LOWER': {'IN': ["to", "till", "until"]}, 'OP': '+'},
                        {'LOWER': {
                            'REGEX': f"^({m})(-)({day_num_pat_regex})$"},
                            'OP': '+'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DURATION'}
                    ),
        ConTextRule(literal="calendar date",
                    category="ENDS_ON",
                    direction="BIDIRECTIONAL",
                    pattern=[
                        {'LOWER': {'IN': ["to", "till", "until"]}, 'OP': '+'},
                        {'LOWER': {
                            'REGEX': f"^({m})(-)({year_num_pat_regex})$"},
                            'OP': '+'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DURATION'}
                    ),
    ])
# exact cal date phrase
for p in patterns.get_rules():
    overlap_rules.extend([
        ConTextRule(literal="calendar date",
                    category="OVERLAP",
                    direction="BIDIRECTIONAL",
                    pattern=[{'LOWER': {'IN': ["on", "at", "of"]}, 'OP': '+'}].extend(p),
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DATE'}
                    ),
    ])
    begin_rules.extend([
        ConTextRule(literal="calendar date",
                    category="BEGINS_ON",
                    direction="BIDIRECTIONAL",
                    pattern=[{'LOWER': {'IN': ["from", "since"]}, 'OP': '+'}].extend(p),
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DATE'}
                    ),
    ])
    end_rules.extend([
        ConTextRule(literal="calendar date",
                    category="ENDS_ON",
                    direction="BIDIRECTIONAL",
                    pattern=[{'LOWER': {'IN': ["to", "till", "until"]}, 'OP': '+'}].extend(p),
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DATE'}
                    ),
    ])

# He losts his home in Jan, 2015 (only month and year but not days)
contain_rules.extend([
    ConTextRule(literal="calendar date",
                category="CONTAINS",
                direction="BIDIRECTIONAL",
                pattern=[{'_': {'concept_tag': 'OF'}, 'OP': '!'},
                         # this is to avoid overlapping span like 'the end of june. 2015'
                         {'LOWER': {'IN': ["for", "about", "in", "during", "between"]}, 'OP': '!'},  # not for 3 months
                         {'LOWER': {'IN': ["since", "in", "within", "during"]}, 'OP': '+'},
                         {"TEXT": {"REGEX": f"({day_num_pat})"}, 'OP': '!'},
                         {'IS_PUNCT': True, 'OP': '*'},
                         {'IS_SPACE': True, 'OP': '*'},
                         {'_': {'concept_tag': 'MONTH'}, 'OP': '+'},
                         {'IS_PUNCT': True, 'OP': '*'},
                         {'IS_SPACE': True, 'OP': '*'},
                         {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '+'}],
                max_scope=maxScope,
                allowed_types=allowed_concept_labels, metadata={'NER': 'DURATION'}
                ),
])

end_rules.extend([
    # (at/until) the end of jan 2015
    ConTextRule(literal="calendar date",
                category="ENDS_ON",
                direction="BIDIRECTIONAL",
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
                max_scope=maxScope,
                allowed_types=allowed_concept_labels, metadata={'NER': 'DURATION'}
                ),

    # at the end of 2015
    ConTextRule(literal="calendar date",
                category="ENDS_ON",
                direction="BIDIRECTIONAL",
                pattern=[{'_': {'concept_tag': "DETERMINER"}, 'OP': '+'},
                         {'_': {'concept_tag': 'END'}, 'OP': '+'},
                         {'_': {'concept_tag': 'OF'}, 'OP': '+'},
                         # this is to avoid overlapping span like 'the end of june. 2015'
                         {'IS_PUNCT': True, 'OP': '*'},
                         {'IS_SPACE': True, 'OP': '*'},
                         {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '+'}],
                max_scope=maxScope,
                allowed_types=allowed_concept_labels, metadata={'NER': 'DURATION'}
                ),
])

begin_rules.extend([
    # (in) the beginning of jan 2015
    ConTextRule(literal="calendar date",
                category="BEGINS_ON",
                direction="BIDIRECTIONAL",
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
                max_scope=maxScope,
                allowed_types=allowed_concept_labels, metadata={'NER': 'DURATION'}
                ),

    # at the beginning of 2015
    ConTextRule(literal="calendar date",
                category="BEGINS_ON",
                direction="BIDIRECTIONAL",
                pattern=[{'_': {'concept_tag': "DETERMINER"}, 'OP': '+'},
                         {'_': {'concept_tag': 'BEGIN'}, 'OP': '+'},
                         {'_': {'concept_tag': 'OF'}, 'OP': '+'},
                         # this is to avoid overlapping span like 'the end of june. 2015'
                         {'IS_PUNCT': True, 'OP': '*'},
                         {'IS_SPACE': True, 'OP': '*'},
                         {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '+'}],
                max_scope=maxScope,
                allowed_types=allowed_concept_labels, metadata={'NER': 'DURATION'}
                ),

])

contain_rules.extend([

    # in 2015
    ConTextRule(literal="in year",
                category="CONTAINS",
                direction="BIDIRECTIONAL",
                pattern=[{'_': {'concept_tag': 'IN'}, 'OP': '+'},
                         {'_': {'concept_tag': 'YEAR'}, 'OP': '+'}],
                max_scope=maxScope,
                allowed_types=allowed_concept_labels, metadata={'NER': 'DURATION'}
                ),

    # on-going (on, -, going)
    ConTextRule(literal="on going",
                category="CONTAINS",
                direction="BIDIRECTIONAL",
                pattern=[{'_': {'concept_tag': 'ON'}, 'OP': '+'},
                         {'LOWER': "-"},
                         {'LOWER': "going", 'OP': '+'}],
                max_scope=maxScope,
                allowed_types=allowed_concept_labels, metadata={'NER': 'DURATION'}
                ),

    #############486
    # for january --line 782
    ConTextRule(literal="month ago",
                category="CONTAINS",
                direction="BIDIRECTIONAL",
                pattern=[{'LOWER': {'IN': ["for", "about", "in", "during", "between", "nearly", "almost"]}, 'OP': '+'},
                         {'_': {'concept_tag': "MONTH"}, 'OP': '+'},
                         {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '!'},
                         {'_': {'concept_tag': "AGO"}, 'OP': '!'}],
                max_scope=maxScope,
                allowed_types=allowed_concept_labels, metadata={'NER': 'DURATION'}
                ),

    # for 2015
    ConTextRule(literal="almost",
                category="CONTAINS",
                direction="BIDIRECTIONAL",
                pattern=[{'LOWER': {'IN': ["for", "about", "in", "during", "between", "nearly", "almost"]}, 'OP': '+'},
                         {"TEXT": {"REGEX": f"({year_num_pat})"}, 'OP': '+'},
                         {'_': {'concept_tag': "AGO"}, 'OP': '!'}],
                max_scope=maxScope,
                allowed_types=allowed_concept_labels, metadata={'NER': 'DURATION'}
                ),
])

for d in duration_concepts:
    contain_rules.extend([
        # (at) sometime this/next time/day/week...,  past 3 weeks: NOT for 3 weeks
        ConTextRule(literal="duration",
                    category="CONTAINS",
                    direction="BIDIRECTIONAL",
                    pattern=[
                        {'LOWER': {'IN': ["for", "about", "in", "during", "between", "nearly", "almost"]}, 'OP': '+'},
                        {'LOWER': {'IN': ["sometime", "later", "earlier"]}, 'OP': '*'},
                        {'LOWER': "the", 'OP': '*'},
                        {'LOWER': {
                            'IN': ['this', 'the', 'next', 'last', 'past', 'previous', 'coming', 'following']},
                            'OP': '+'},
                        {'LOWER': "of", 'OP': '*'},
                        {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '*'},
                        {'_': {'concept_tag': d}, 'OP': '+'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DURATION'}
                    ),

        # (at) this/next time/day/week...,  past three weeks
        ConTextRule(literal="duration",
                    category="CONTAINS",
                    direction="BIDIRECTIONAL",
                    pattern=[{'LOWER': {'IN': ["for", "about", "in", "during", "between"]}, 'OP': '!'},
                             {'LOWER': {'IN': ["sometime", "later", "earlier"]}, 'OP': '*'},
                             {'LOWER': "the", 'OP': '*'},
                             {'LOWER': {
                                 'IN': ['this', 'the', 'next', 'last', 'past', 'previous', 'coming', 'following']},
                                 'OP': '+'},
                             {'_': {'concept_tag': 'NUMBER'}, 'OP': '+'},
                             {'_': {'concept_tag': d}, 'OP': '+'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DURATION'}
                    ),

        # in this year, in june, in this week ...
        ConTextRule(literal="vague date",
                    category="CONTAINS",
                    direction="BIDIRECTIONAL",
                    pattern=[{'_': {'concept_tag': 'IN'}, 'OP': '+'},
                            {'_': {'concept_tag': "DETERMINER"}, 'OP': '*'},
                            {'_': {'concept_tag': d}, 'OP': '+'}, ],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DURATION'}
                    ),

        # couple of days
        ConTextRule(literal="couple of days",
                    category="CONTAINS",
                    direction="BIDIRECTIONAL",
                    pattern=[
                        {'LOWER': {'IN': ["the", "a"]}, 'OP': '*'},
                        {'LOWER': {
                            'IN': ['this', 'next', 'last', 'past', 'previous', 'coming', 'following']},
                            'OP': '*'},
                        {'LOWER': {'IN': ['few', 'several', 'couple']}, 'OP': '+'},
                        {'LOWER': "of", 'OP': '*'},
                        {'_': {'concept_tag': d}, 'OP': '+'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DURATION'}
                    ),

        # (at) this/next time/day/week...,  for past three weeks
        ConTextRule(literal="for the past",
                    category="CONTAINS",
                    direction="BIDIRECTIONAL",
                    pattern=[
                        {'LOWER': {'IN': ["for", "about", "in", "during", "between", "nearly", "almost"]}, 'OP': '+'},
                        {'LOWER': {'IN': ["sometime", "later", "earlier"]}, 'OP': '*'},
                        {'LOWER': "the", 'OP': '*'},
                        {'LOWER': {
                            'IN': ['this', 'the', 'next', 'last', 'past', 'previous', 'coming', 'following', 'several',
                                   'couple']},
                            'OP': '+'},
                        {'LOWER': "of", 'OP': '*'},
                        {'_': {'concept_tag': 'NUMBER'}, 'OP': '+'},
                        {'_': {'concept_tag': d}, 'OP': '+'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DURATION'}
                    ),

        # 2 days, 2 minutes ...
        ConTextRule(literal="2 days",
                    category="CONTAINS",
                    direction="BIDIRECTIONAL",
                    pattern=[
                        {'LOWER': {'IN': ["for", "about", "in", "during", "between", "nearly", "almost"]}, 'OP': '*'},
                        {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                        {'_': {'concept_tag': d}, 'OP': '+'},
                        {'_': {'concept_tag': "AGO"}, 'OP': '!'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DURATION'}
                    ),

        # two days
        ConTextRule(literal="two days",
                    category="CONTAINS",
                    direction="BIDIRECTIONAL",
                    pattern=[
                        {'LOWER': {'IN': ["for", "about", "in", "during", "between", "nearly", "almost"]}, 'OP': '*'},
                        {'_': {'concept_tag': 'NUMBER'}, 'OP': '+'},
                        {'_': {'concept_tag': d}, 'OP': '+'},
                        {'_': {'concept_tag': "AGO"}, 'OP': '!'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DURATION'}
                    ),

        # 4 and one half years since
        ConTextRule(literal="duration",
                    category="CONTAINS",
                    direction="BIDIRECTIONAL",
                    pattern=[{'LOWER': {'IN': ["for", "about", "in", "during", "between", "nearly", "almost", "from"]},
                              'OP': '*'},
                             {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                             {'LOWER': "and", 'OP': '+'},
                             {'LOWER': "one", 'OP': '+'},
                             {'LOWER': "half", 'OP': '+'},
                             {'_': {'concept_tag': d}, 'OP': '+'},
                             {'_': {'concept_tag': "AGO"}, 'OP': '!'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DURATION'}
                    ),

        # 37 5/7 week
        ConTextRule(literal="in year",
                    category="CONTAINS",
                    direction="BIDIRECTIONAL",
                    pattern=[
                        {'LOWER': {'IN': ["for", "about", "in", "during", "between", "nearly", "almost"]}, 'OP': '*'},
                        {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                        {'LOWER': 'and', 'OP': '*'},
                        {"TEXT": {"REGEX": "^[1-9]/[1-9]$"}, 'OP': '+'},
                        {'_': {'concept_tag': d}, 'OP': '+'},
                        {'_': {'concept_tag': "AGO"}, 'OP': '!'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DURATION'}
                    ),
        # another week
        ConTextRule(literal="another week",
                    category="CONTAINS",
                    direction="BIDIRECTIONAL",
                    pattern=[{'LOWER': {'IN': ["for", "about", "in", "during", "between", "nearly", "almost", "from"]},
                              'OP': '*'},
                             {'LOWER': "another", 'OP': '+'},
                             {'_': {'concept_tag': d}, 'OP': '+'},
                             {'_': {'concept_tag': "AGO"}, 'OP': '!'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DURATION'}
                    ),

        # 1 to 3 days
        ConTextRule(literal="1 to 3 days",
                    category="CONTAINS",
                    direction="BIDIRECTIONAL",
                    pattern=[{'LOWER': {'IN': ["for", "about", "in", "during", "between", "nearly", "almost", "from"]},
                              'OP': '*'},
                             {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                             {'LOWER': "to", 'OP': '+'},
                             {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                             {'_': {'concept_tag': d}, 'OP': '+'},
                             {'_': {'concept_tag': "AGO"}, 'OP': '!'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DURATION'}
                    ),

        # one to three days
        ConTextRule(literal="# one to three days",
                    category="CONTAINS",
                    direction="BIDIRECTIONAL",
                    pattern=[{'LOWER': {'IN': ["for", "about", "in", "during", "between", "nearly", "almost", "from"]},
                              'OP': '*'},
                             {'_': {'concept_tag': 'NUMBER'}, 'OP': '+'},
                             {'LOWER': "to", 'OP': '+'},
                             {'_': {'concept_tag': 'NUMBER'}, 'OP': '+'},
                             {'_': {'concept_tag': d}, 'OP': '+'},
                             {'_': {'concept_tag': "AGO"}, 'OP': '!'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DURATION'}
                    ),

        # 1-3 days
        ConTextRule(literal=" # 1-3 days",
                    category="CONTAINS",
                    direction="BIDIRECTIONAL",
                    pattern=[{'LOWER': {'IN': ["for", "about", "in", "during", "between", "nearly", "almost", "from"]},
                              'OP': '*'},
                             {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                             {'LOWER': "-", 'OP': '+'},
                             {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                             {'_': {'concept_tag': d}, 'OP': '+'},
                             {'_': {'concept_tag': "AGO"}, 'OP': '!'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DURATION'}
                    ),
        # at least 3 days
        ConTextRule(literal="at least 3 days",
                    category="CONTAINS",
                    direction="BIDIRECTIONAL",
                    pattern=[
                        {'LOWER': {'IN': ["for", "about", "in", "during", "between", "nearly", "almost"]}, 'OP': '*'},
                        {'LOWER': "at", 'OP': '+'},
                        {'LOWER': "least", 'OP': '+'},
                        {'LOWER': {'IN': ["for", "about", "in", "during"]}, 'OP': '*'},
                        {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                        {'_': {'concept_tag': d}, 'OP': '+'},
                        {'_': {'concept_tag': "AGO"}, 'OP': '!'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DURATION'}
                    ),
        # at least three days
        ConTextRule(literal="at least three days",
                    category="CONTAINS",
                    direction="BIDIRECTIONAL",
                    pattern=[
                        {'LOWER': {'IN': ["for", "about", "in", "during", "between", "nearly", "almost"]}, 'OP': '*'},
                        {'LOWER': "at", 'OP': '+'},
                        {'LOWER': "least", 'OP': '+'},
                        {'LOWER': {'IN': ["for", "about", "in", "during"]}, 'OP': '*'},
                        {'_': {'concept_tag': 'NUMBER'}, 'OP': '+'},
                        {'_': {'concept_tag': d}, 'OP': '+'},
                        {'_': {'concept_tag': "AGO"}, 'OP': '!'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DURATION'}
                    ),
        # more than (less than) 3 days
        ConTextRule(literal="more than (less than) 3 days",
                    category="CONTAINS",
                    direction="BIDIRECTIONAL",
                    pattern=[
                        {'LOWER': {'IN': ["for", "about", "in", "during", "between", "nearly", "almost"]}, 'OP': '*'},
                        {'LOWER': {'IN': ["more", "less"]}, 'OP': '+'},
                        {'LOWER': "than", 'OP': '+'},
                        {'LOWER': {'IN': ["for", "about", "in", "during"]}, 'OP': '*'},
                        {"TEXT": {"REGEX": "^[0-9]|[0-9][0-9]$"}, 'OP': '+'},
                        {'_': {'concept_tag': d}, 'OP': '+'},
                        {'_': {'concept_tag': "AGO"}, 'OP': '!'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DURATION'}
                    ),
        # more than three days
        ConTextRule(literal="more than three days",
                    category="CONTAINS",
                    direction="BIDIRECTIONAL",
                    pattern=[
                        {'LOWER': {'IN': ["for", "about", "in", "during", "between", "nearly", "almost"]}, 'OP': '*'},
                        {'LOWER': {'IN': ["more", "less"]}, 'OP': '+'},
                        {'LOWER': "than", 'OP': '+'},
                        {'LOWER': {'IN': ["for", "about", "in", "during"]}, 'OP': '*'},
                        {'_': {'concept_tag': 'NUMBER'}, 'OP': '+'},
                        {'_': {'concept_tag': d}, 'OP': '+'},
                        {'_': {'concept_tag': "AGO"}, 'OP': '!'}],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DURATION'}
                    ),

    ])



begin_rules = []
for d in duration_concepts:
    begin_rules.extend([
        #from this day
        ConTextRule(literal="date",
                    category="BEGINS_ON",
                    direction="BIDIRECTIONAL",
                    pattern=[{'LOWER': {'IN': ["from"]}, 'OP': '+'},
                             {'LOWER': "the", 'OP': '*'},
                             {'LOWER': {
                                 'IN': ['this', 'the', 'next', 'last', 'past', 'previous', 'coming', 'following']},
                                 'OP': '*'},
                             {'_': {'concept_tag': d}, 'OP': '+'}
                             ],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DATE'}
                    ),

        # at the beginnin of this day
        ConTextRule(literal="date",
                    category="BEGINS_ON",
                    direction="BIDIRECTIONAL",
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
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DATE'}
                    ),

    ])

end_rules = []
for d in duration_concepts:
    end_rules.extend([
        # until this day
        ConTextRule(literal="date",
                    category="ENDS_ON",
                    direction="BIDIRECTIONAL",
                    pattern=[{'LOWER': {'IN': ["until", "till"]}, 'OP': '+'},
                             {'LOWER': "the", 'OP': '*'},
                             {'LOWER': {
                                 'IN': ['this', 'the', 'next', 'last', 'past', 'previous', 'coming', 'following']},
                                 'OP': '*'},
                             {'_': {'concept_tag': d}, 'OP': '+'}
                             ],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DATE'}
                    ),

        # until December
        ConTextRule(literal="calendar date",
                    category="ENDS_ON",
                    direction="BIDIRECTIONAL",
                    pattern=[{'LOWER': {'IN': ["until", "till"]}, 'OP': '+'},
                             {'LOWER': "the", 'OP': '*'},
                             {'LOWER': {
                                 'IN': ['this', 'the', 'next', 'last', 'past', 'previous', 'coming', 'following']},
                                 'OP': '*'},
                             {'_': {'concept_tag': d}, 'OP': '+'}
                             ],
                    max_scope=maxScope,
                    allowed_types=allowed_concept_labels, metadata={'NER': 'DATE'}
                    ),
    ])


def get_ConText_rules():
    return contain_rules + overlap_rules + begin_rules + end_rules
