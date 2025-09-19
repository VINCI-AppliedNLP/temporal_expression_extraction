from medspacy.ner import TargetRule

num_word_token = ["zero",
                  "one",
                  "two",
                  "three",
                  "four",
                  "five",
                  "six",
                  "seven",
                  "eight",
                  "nine",
                  "ten",
                  "eleven",
                  "twelve",
                  "thirteen",
                  "fourteen",
                  "fifteen",
                  "sixteen",
                  "seventeen",
                  "eighteen",
                  "nineteen",
                  "twenty"]

ordinal_num_token = ["first",
                     "1st",
                     "second",
                     "2nd",
                     "third",
                     "3rd",
                     "fourth",
                     "4th",
                     "fifth",
                     "5th",
                     "sixth",
                     "6th",
                     "seventh",
                     "7th",
                     "eighth",
                     "8th",
                     "ninth",
                     "9th",
                     "tenth",
                     "10th",
                     "11th",
                     "12th",
                     "13th",
                     "14th",
                     "15th",
                     "16th",
                     "17th",
                     "18th",
                     "19th",
                     "20th",
                     "21st",
                     "22nd",
                     "23rd",
                     "24th",
                     "25th",
                     "26th",
                     "27th",
                     "28th",
                     "29th",
                     "30th",
                     "31st"]

month_token = ["month",
               "months",
               "january",
               "jan",
               "february",
               "feb",
               "march",
               "mar",
               "april",
               "apr",
               "may",
               "june",
               "jun",
               "july",
               "jul",
               "august",
               "aug",
               "september",
               "sep",
               "october",
               "oct",
               "november",
               "nov",
               "december",
               "dec"]

cal_date = ["today", "tonight", "night", "morning", "evening", "afternoon", "tomorrow", "yesterday", "current", "currently", "now",
            "recent", "recently",  "future", "present", "still"] #"present", "still",

time_token = ["am", "pm", "a.m", 'p.m', "o'clock", "time"]

second_token = ["second", "seconds", "sec"]

minute_token = ["minute", "minutes", "min"]

hour_token = ["hour", "hours", "hrs"]

year_token = ["year", "years", "yrs"]

day_token = ["days", "day"]

week_token = ["week", "wks", "weeks"]

week_name_token = ["monday", "tuesday", 'wednesday', "thursday", "friday", "saturday", "sunday", "mon", "tue", "wed",
                   "thur", "fri", "sat", "sun"]

frequency_token = ["daily", "weekly", "monthly", "yearly", "quarterly", "b.i.d", "tid", "t.i.d", "bid", "p.r.n", "prn", "qd", "qhs", "q.h.s"]

frequency_unit_token = ["times", "episodes"]

determiner_token = ["every", "each", "a", "an", "this", "the", "per"]

prep_token = {"since": "SINCE",
              "in": "IN",
              "at": "AT",
              "on": "ON",
              "about": "ABOUT",
              "within": "WITHIN",
              "from": "FROM",
              "to": "TO",
              "till": "TILL",
              "until": "UNTIL",
              "of": "OF",
              "during": "DURING",
              "or": "OR"}

order_token = {"last": "LAST",
               "past": "PAST",
               "next": "NEXT",
               "ago": "AGO",
               "end": "END",
               "beginning": "BEGIN"}

month_pat = "|".join(month_token)

'''
REMARK: SpaCy's EntityRuler cannot use RegEx to pattern match accross tokens
'''

month_num_pat = "(^1[0-2]$)|(^0?\d$)"  #"1[0-2]|0?\\d" #token pattern to NER
day_num_pat = "(^0[1-9]$)|(^[12][0-9]$)|(^3[01]$)"  #"?<![0-9])([0-2]?\\d|30|31" # token pattern for NER
year_num_pat = "(^[12]\d{3}$)|(^\d{2}$)"  #"([12]\\d{3})|(\\d{2})"  #1999 or 99 # token pattern for NER
sep_pat = "(^\\.$)|(^/$)|(^\\\\$)" #"\\.|/|\\\\"  #\\. matches .; / matches /; \\\\matches / # token pattern for NER

# --------- calendar date tokens
month_num_pat_regex = "1[0-2]|0?\\d" #part of regex not part of token
day_num_pat_regex = "?<![0-9])([0-2]?\\d|30|31"
year_num_pat_regex = "([12]\\d{3})|(\\d{2})"
sep_pat_regex = "\\.|/|\\\\"  #\\. matches .; / matches /; \\\\matches /

# Separator in calendar rules needs to be consistent such as 1.15.2018 not 1/15.2018
cal_date_rules = []
for sep in ['\\.','/','\\\\']: # 3 types of separators
    cal_date_rules.extend([
        TargetRule(literal="calendar date",
                   category="CAL_DATE",
                   pattern=[
                       {'LOWER': {
                           'REGEX': f"({day_num_pat_regex})({sep})({month_num_pat_regex})({sep})({year_num_pat_regex})"}}],
                   attributes=None,
                   on_match=None),

        TargetRule(literal="calendar date",
                   category="CAL_DATE",
                   pattern=[
                       {'LOWER': {
                           'REGEX': f"({month_num_pat_regex})({sep})({day_num_pat_regex})({sep})({year_num_pat_regex})"}}],
                   attributes=None,
                   on_match=None),

        TargetRule(literal="calendar date",
                   category="CAL_DATE",
                   pattern=[
                       {'LOWER': {
                           'REGEX': f"({year_num_pat_regex})({sep})({month_num_pat_regex})({sep})({day_num_pat_regex})"}}],
                   attributes=None,
                   on_match=None),

        TargetRule(literal="calendar date",
                   category="CAL_DATE",
                   pattern=[
                       {'LOWER': {
                           'REGEX': f"({year_num_pat_regex})({sep})({day_num_pat_regex})({sep})({month_num_pat_regex})"}}],
                   attributes=None,
                   on_match=None),
    ])

#---------inexplicite calendar date
cal_date_rules.append(
    # it is rare expression 5/18 . pattern sep_pat_regex = "\\.|/|\\\\"  #\\. matches .; / matches /; \\\\matches /
    TargetRule(literal="calendar date",
               category="CAL_DATE",
               pattern=[
                   {'LOWER': {'REGEX': f"^({month_num_pat_regex})(/|\\\\)({day_num_pat_regex})$"}}],
               attributes=None,
               on_match=None),
                   )
# --------inexplicite date like OCT-99 or OCT-10, this will be parsed into one token
for m in month_token:
    cal_date_rules.extend([
        TargetRule(literal="calendar date",
                   category="CAL_DATE",
                   pattern=[
                       {'LOWER': {'REGEX': f"^({m})(-)({day_num_pat_regex})$"}}],
                   attributes=None,
                   on_match=None),

        TargetRule(literal="calendar date",
                   category="CAL_DATE",
                   pattern=[
                       {'LOWER': {'REGEX': f"^({m})(-)({year_num_pat_regex})$"}}],
                   attributes=None,
                   on_match=None),
        ]
    )


# --------- implicit calendar date tokens
implicit_cal_date_rules = []
for w in cal_date:
    implicit_cal_date_rules.append(
        TargetRule(literal=w, category="CAL_DATE", pattern=[{"LOWER": w}], attributes=None, on_match=None))

# --------- number words tokens
num_word_rules = []
for num in num_word_token:
    num_word_rules.append(
        TargetRule(literal=num, category="NUMBER", pattern=[{"LOWER": num}], attributes=None, on_match=None))

# --------- ordinal number token
ordinal_num_rules = []
for ordinal in ordinal_num_token:
    ordinal_num_rules.append(
        TargetRule(literal=ordinal, category="ORDINAL", pattern=[{"LOWER": ordinal}], attributes=None, on_match=None))

# --------- time unit tokens
time_rules = []
for t in time_token:
    time_rules.append(TargetRule(literal=t, category="TIME", pattern=[{"LOWER": t}], attributes=None, on_match=None))

# --------- second, minute, hour tokens
sec_min_hour_rules = []
for s in second_token:
    sec_min_hour_rules.append(
        TargetRule(literal=s, category="SECOND", pattern=[{"LOWER": s}], attributes=None, on_match=None))
for m in minute_token:
    sec_min_hour_rules.append(
        TargetRule(literal=m, category="MINUTE", pattern=[{"LOWER": m}], attributes=None, on_match=None))
for h in hour_token:
    sec_min_hour_rules.append(
        TargetRule(literal=h, category="HOUR", pattern=[{"LOWER": h}], attributes=None, on_match=None))

# --------- day tokens
day_rules = []
for d in day_token:
    day_rules.append(TargetRule(literal=d, category="DAY", pattern=[{"LOWER": d}], attributes=None, on_match=None))

# --------- week tokens
week_rules = []
for wk in week_token:
    week_rules.append(TargetRule(literal=wk, category="WEEK", pattern=[{"LOWER": wk}], attributes=None, on_match=None))

# --------- week name tokens
week_name_rules = []
for wn in week_name_token:
    week_name_rules.append(
        TargetRule(literal=wn, category="CAL_DATE", pattern=[{"LOWER": wn}], attributes=None, on_match=None))

# --------- month tokens
month_rules = []
for m in month_token:
    month_rules.append(TargetRule(literal=m, category="MONTH", pattern=[{"LOWER": m}], attributes=None, on_match=None))

# --------- year tokens
year_rules = []
for y in year_token:
    year_rules.append(TargetRule(literal=y, category="YEAR", pattern=[{"LOWER": y}], attributes=None, on_match=None))

# --------- frequency
frequency_rules = []
for f in frequency_token:
    frequency_rules.append(
        TargetRule(literal=f, category="FREQUENCY", pattern=[{"LOWER": f}], attributes=None, on_match=None))

# --------- frequency unit
frequency_unit_rules = []
for fu in frequency_unit_token:
    frequency_unit_rules.append(
        TargetRule(literal=fu, category="FREQUENCY_UNIT", pattern=[{"LOWER": fu}], attributes=None, on_match=None))

# --------- ORDER
order_rules = []
for order in order_token.keys():
    order_rules.append(
        TargetRule(literal=order, category=order_token[order], pattern=[{"LOWER": order}], attributes=None,
                   on_match=None)
    )

# --------- PREPOSITION
prep_rules = []
for p in prep_token.keys():  #Dictionary
    prep_rules.append(
        TargetRule(literal=p, category=prep_token[p], pattern=[{"LOWER": p}], attributes=None, on_match=None))

# --------- DETERMINER
determiner_rules = []
for d in determiner_token:
    determiner_rules.append(
        TargetRule(literal=d, category="DETERMINER", pattern=[{"LOWER": d}], attributes=None, on_match=None))


####### all the rules
def get_token_rules():
    return (cal_date_rules +
            implicit_cal_date_rules +
            num_word_rules +
            ordinal_num_rules +
            time_rules +
            sec_min_hour_rules +
            day_rules +
            week_rules +
            week_name_rules +
            month_rules +
            year_rules +
            frequency_rules +
            frequency_unit_rules +
            order_rules +
            prep_rules +
            determiner_rules)



