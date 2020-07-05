"""Verb conjugation in French is a hugely complicated process
genreally, and even more so for irregular verbs. This file attempts to
organize all the variations and compress them to common patterns."""


# French Conjugation Patterns for use in conjugator_fr
f_conj_pat = [
                 [0, 0, 0, 1, 1, 2],
                 [0, 0, 0, 0, 0, 0],
             ]

# List of various possible endings of different verbs.
endings = [
              ['s', 's', 't', 'ons', 'ez', 'ent'],
              ['u', 'u', 'u', 'u', 'u', 'u'],
              ['ais', 'ais', 'ait', 'ions', 'iez', 'aient'],
              ['s', 's', 't', 'mes', 'tes', 'ent'],
              ['ai', 'as', 'a', 'ons', 'ez', 'ont']
          ]

frenchverb_irr_first = {
    "tenir": {
                'ind': {
                    'p': (f_conj_pat[0], ['tien', 'ten', 'tienn'], endings[0]),
                    'pc': (f_conj_pat[1], ['ten'], endings[1]),
                    'i': (f_conj_pat[1], ['ten'], endings[2]),
                    'pqp': (f_conj_pat[1], ['ten'], endings[1]),
                    'ps': (f_conj_pat[1], ['tin', 'tîn', 'tinr'], endings[3]),
                    'pa': (f_conj_pat[0], ['ten'], endings[1]),
                    'fs': (f_conj_pat[0], ['tiendr'], endings[4]),
                    'fa': (f_conj_pat[0], ['ten'], endings[1]),
                },
                'subjonctif': {
                    'p': 'TO BE DEVELOPED',
                    'passé': 'TO BE DEVELOPED',
                    'i': 'TO BE DEVELOPED',
                    'pqp': 'TO BE DEVELOPED',
                },
                'conditionnel': {
                    'p': 'TO BE DEVELOPED',
                    'passé 1': 'TO BE DEVELOPED',
                    'passé 2': 'TO BE DEVELOPED',
                },
                'impératif': {
                    'p': {
                        's2': 'TO BE DEVELOPED',
                        'p1': 'TO BE DEVELOPED',
                        'p2': 'TO BE DEVELOPED'
                    },
                    'passé': {
                        's2': 'TO BE DEVELOPED',
                        'p1': 'TO BE DEVELOPED',
                        'p2': 'TO BE DEVELOPED'
                    }
                },
                'participe': {
                    'présent': '',
                    'passé': ''
                },
                'infinitif': {
                    'présent': '',
                    'passé': ''
                },
                'gérondif': {
                    'présent': '',
                    'passé': ''
                }
             }
        }
 