from medspacy.context import ConTextRule, ConText
import temporal_token_rules

overlap_rules = [
    ConTextRule(literal = "current",
                category = "CONTAIN",
                direction="FORWARD",
                ),
]