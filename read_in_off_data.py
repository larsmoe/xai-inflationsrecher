import numpy as np

weights = np.array(['Nahrungsmittel und\nalkoholfreie Getränke',
'Alkoholische\nGetränke',
'Restaurants, Cafés',
'Nettokaltmiete',
'Strom',
'Gas',
'Heizöl',
'Neu- und Ge-\nbrauchtwagenkauf',
'Kraftstoffe und\nFahrzeugwartung',
'Öffentl.\nVerkehrsmittel',
'Freizeit /Kultur',
'Pauschalreisen',
'Tabakwaren',
'Bekleidung\nund Schuhe',
'Elektrogeräte',
'Gesundheit',
'Telekommunikations-\ndienstleistungen',
'Körperpflege',
'Rest'
])
np.save('categories.npy', weights)