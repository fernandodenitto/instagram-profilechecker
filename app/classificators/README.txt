In questo file spiego come importare il classificatore nell'applicazione

IMPORTARE IL MODULO PICKLE

import pickle

CARICARE IL MODELLO DI classificatore

classificator = pickle.load(open(filename, 'rb'))

NEL CASO DEL CLASSIFICATORE CHE USEREMO SARÀ UN DECISION TREE CHE SI TROVA 
NELLA DIRECTORY CLASSIFICATORS

A REGOLA QUINDI FILENAME È QUESTO

'./classificators/DT_without_stats.sav'

UNA VOLTA IMPORTATO E QUINDI CARICATO, IL RISULTATO DELLA CLASSIFICAZIONE S
SI OTTIENE SEMPLICEMENTE CHIAMANDO LA FUNZIONE PREDICT DELL'ALBERO DUNQUE:

classificator.predict(input)

NOTA BENE SULL'INPUT:
È un classificatore solo sulle info generali che a regola sono 11 ed il formato
che deve essere passato è come il seguente:

[[True 120 925 52281 56.52 1473 False False False False 8]]

QUINDI UNA LISTA DI ARRAY (CREDO)

IL RITORNO È INFATTI UN ARRAY DI RISULTATI DI CLASSIFICAZIONE DEL TIPO:

array([ True])

ALLA GRANDE SOCIO! 



