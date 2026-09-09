#!/usr/bin/env python3
"""Generate Saw 7X landing, thank-you and redirect pages for CZ/ES/HU/IT/PL/PT."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

GEOS = {
    "cz": {
        "lang": "cs",
        "currency": "CZK",
        "price": 1899,
        "schema_price": "1899",
        "price_display": "1 899 Kč",
        "old_price_display": "3 798 Kč",
        "country": "Česko",
        "country_prep": "po celé ČR",
    },
    "es": {
        "lang": "es",
        "currency": "EUR",
        "price": 79,
        "schema_price": "79.00",
        "price_display": "79,00€",
        "old_price_display": "158,00€",
        "country": "España",
        "country_prep": "en toda España",
    },
    "hu": {
        "lang": "hu",
        "currency": "HUF",
        "price": 29999,
        "schema_price": "29999",
        "price_display": "29 999 Ft",
        "old_price_display": "59 998 Ft",
        "country": "Magyarország",
        "country_prep": "egész Magyarországon",
    },
    "it": {
        "lang": "it",
        "currency": "EUR",
        "price": 79.99,
        "schema_price": "79.99",
        "price_display": "79,99€",
        "old_price_display": "159,98€",
        "country": "Italia",
        "country_prep": "in tutta Italia",
    },
    "pl": {
        "lang": "pl",
        "currency": "PLN",
        "price": 339,
        "schema_price": "339",
        "price_display": "339 zł",
        "old_price_display": "678 zł",
        "country": "Polska",
        "country_prep": "w całej Polsce",
    },
    "pt": {
        "lang": "pt",
        "currency": "EUR",
        "price": 99,
        "schema_price": "99.00",
        "price_display": "99,00€",
        "old_price_display": "198,00€",
        "country": "Portugal",
        "country_prep": "em todo o Portugal",
    },
}

# Italian source string → translations (IT kept only when the target must change with price/country).
T = {
    "cz": {},
    "es": {},
    "hu": {},
    "pl": {},
    "pt": {},
}

def add(it: str, **langs: str) -> None:
    for geo, text in langs.items():
        T[geo][it] = text


add(
    "OGGI IN SCONTO AL 50%",
    cz="DNES SLEVA 50 %",
    es="HOY CON 50% DE DESCUENTO",
    hu="MA 50% KEDVEZMÉNNYEL",
    pl="DZIŚ 50% TANIEJ",
    pt="HOJE COM 50% DE DESCONTO",
)
add(
    "✅ Pagamento alla consegna · Spedizione gratuita 24/48h",
    cz="✅ Platba na dobírku · Doprava zdarma 24/48h",
    es="✅ Pago contra reembolso · Envío gratis 24/48h",
    hu="✅ Utánvétes fizetés · Ingyenes szállítás 24/48h",
    pl="✅ Płatność przy odbiorze · Darmowa dostawa 24/48h",
    pt="✅ Pagamento na entrega · Envio grátis 24/48h",
)
add(
    "Taglia i rami più alti e i tronchi più grossi senza scala.",
    cz="Řežte nejvyšší větve i silné kmeny bez žebříku.",
    es="Corta las ramas más altas y los troncos más gruesos sin escalera.",
    hu="Vágja a legmagasabb ágakat és a vastag törzseket létra nélkül.",
    pl="Przycinaj najwyższe gałęzie i grube pnie bez drabiny.",
    pt="Corte os ramos mais altos e os troncos mais grossos sem escada.",
)
add(
    "Senza benzina. Senza fatica. Fino a 5 metri.",
    cz="Bez benzínu. Bez dřiny. Až 5 metrů.",
    es="Sin gasolina. Sin esfuerzo. Hasta 5 metros.",
    hu="Benzin nélkül. Erőfeszítés nélkül. Akár 5 méterig.",
    pl="Bez benzyny. Bez wysiłku. Do 5 metrów.",
    pt="Sem gasolina. Sem esforço. Até 5 metros.",
)
add(
    "Saw 7X™: motosega elettrica telescopica. In pochi secondi passa dal modo manuale compatto all’asta. Taglia il legno fino a <b>35 cm</b> di diametro, arriva a <b>5 metri</b> e pesa solo <b>700 g</b>. Fatta per il giardino, gli alberi da frutto e lo spazio intorno a casa.",
    cz="Saw 7X™: elektrická teleskopická pila. Během několika sekund přepnete z kompaktního ručního režimu na tyč. Řeže dřevo o průměru až <b>35 cm</b>, dosáhne do <b>5 metrů</b> a váží jen <b>700 g</b>. Stvořená pro zahradu, ovocné stromy a prostor kolem domu.",
    es="Saw 7X™: motosierra eléctrica telescópica. En pocos segundos pasa del modo manual compacto a la pértiga. Corta madera de hasta <b>35 cm</b> de diámetro, llega a <b>5 metros</b> y pesa solo <b>700 g</b>. Hecha para el jardín, los frutales y el entorno de casa.",
    hu="Saw 7X™: teleszkópos elektromos láncfűrész. Néhány másodperc alatt vált kompakt kézi módból rúdra. Akár <b>35 cm</b> átmérőjű fát vág, <b>5 méterig</b> elér, és csak <b>700 g</b>. Kerthez, gyümölcsfákhoz és a ház körüli területhez készült.",
    pl="Saw 7X™: elektryczna pilarka teleskopowa. W kilka sekund przechodzi z trybu ręcznego na wysięgnik. Tnie drewno o średnicy do <b>35 cm</b>, sięga na <b>5 metrów</b> i waży tylko <b>700 g</b>. Stworzona do ogrodu, drzew owocowych i przestrzeni wokół domu.",
    pt="Saw 7X™: motosserra elétrica telescópica. Em poucos segundos passa do modo manual compacto para a haste. Corta madeira até <b>35 cm</b> de diâmetro, chega a <b>5 metros</b> e pesa só <b>700 g</b>. Feita para o jardim, as árvores de fruto e o espaço em volta de casa.",
)
add(
    "Restano solo <strong>4 kit</strong> a questo prezzo",
    cz="Zbývají jen <strong>4 sady</strong> za tuto cenu",
    es="Quedan solo <strong>4 kits</strong> a este precio",
    hu="Már csak <strong>4 készlet</strong> maradt ezen az áron",
    pl="Zostały tylko <strong>4 zestawy</strong> w tej cenie",
    pt="Restam só <strong>4 kits</strong> neste preço",
)
add(
    "<strong>3.000 W e asta telescopica fino a 5 metri.</strong>",
    cz="<strong>3 000 W a teleskopická tyč až 5 metrů.</strong>",
    es="<strong>3.000 W y pértiga telescópica de hasta 5 metros.</strong>",
    hu="<strong>3 000 W és teleszkópos rúd akár 5 méterig.</strong>",
    pl="<strong>3000 W i wysięgnik teleskopowy do 5 metrów.</strong>",
    pt="<strong>3.000 W e haste telescópica até 5 metros.</strong>",
)
add(
    "Dove un decespugliatore normale si ferma, la Saw 7X™ continua. Attraversa legno verde o secco, rami grossi e tronchi fino a 35 cm.",
    cz="Tam, kde se běžný křovinořez zastaví, Saw 7X™ pokračuje. Projde zeleným i suchým dřevem, silnými větvemi i kmeny až do 35 cm.",
    es="Donde una desbrozadora normal se detiene, la Saw 7X™ sigue. Atraviesa madera verde o seca, ramas gruesas y troncos de hasta 35 cm.",
    hu="Ahol egy sima fűkasza megáll, a Saw 7X™ folytatja. Átvágja a zöld és száraz fát, vastag ágakat és akár 35 cm-es törzseket.",
    pl="Tam, gdzie zwykła wykaszarka się zatrzymuje, Saw 7X™ idzie dalej. Przecina zielone i suche drewno, grube gałęzie i pnie do 35 cm.",
    pt="Onde um corta-mato normal pára, a Saw 7X™ continua. Atravessa madeira verde ou seca, ramos grossos e troncos até 35 cm.",
)
add(
    "<strong>2 batterie da 48 V e 8.000 mAh.</strong>",
    cz="<strong>2 baterie 48 V a 8 000 mAh.</strong>",
    es="<strong>2 baterías de 48 V y 8.000 mAh.</strong>",
    hu="<strong>2 darab 48 V-os, 8000 mAh-s akkumulátor.</strong>",
    pl="<strong>2 akumulatory 48 V i 8000 mAh.</strong>",
    pt="<strong>2 baterias de 48 V e 8.000 mAh.</strong>",
)
add(
    "Una al lavoro, l’altra in carica in 45 min. Niente benzina, niente miscela, niente cavi tra i piedi.",
    cz="Jedna pracuje, druhá se nabije za 45 min. Žádný benzín, žádná směs, žádné kabely pod nohama.",
    es="Una trabaja, la otra carga en 45 min. Sin gasolina, sin mezcla, sin cables por medio.",
    hu="Az egyik dolgozik, a másik 45 perc alatt tölt. Nincs benzin, nincs keverék, nincsenek kábelek a láb alatt.",
    pl="Jeden pracuje, drugi ładuje się w 45 min. Bez benzyny, bez mieszanki, bez kabli pod nogami.",
    pt="Uma a trabalhar, a outra a carregar em 45 min. Sem gasolina, sem mistura, sem cabos pelos pés.",
)
add(
    "<strong>Pesa 700 g — la controlli con una mano.</strong>",
    cz="<strong>Váží 700 g — ovládáte ji jednou rukou.</strong>",
    es="<strong>Pesa 700 g: la controlas con una mano.</strong>",
    hu="<strong>700 g — egy kézzel irányítja.</strong>",
    pl="<strong>Waży 700 g — sterujesz jedną ręką.</strong>",
    pt="<strong>Pesa 700 g — controla-a com uma mão.</strong>",
)
add(
    "Meno fatica su braccia, spalle e schiena, anche nei lavori più lunghi. Freno istantaneo.",
    cz="Méně námahy na paže, ramena i záda i při delší práci. Okamžitá brzda.",
    es="Menos esfuerzo en brazos, hombros y espalda, también en los trabajos más largos. Freno instantáneo.",
    hu="Kevesebb terhelés a karokon, vállon és háton, még hosszabb munkánál is. Azonnali fék.",
    pl="Mniej obciążenia ramion, barków i pleców, także przy dłuższej pracy. Natychmiastowy hamulec.",
    pt="Menos esforço em braços, ombros e costas, mesmo nos trabalhos mais longos. Travão instantâneo.",
)
add(
    "<strong>SuperChain X™ lubrifica e tende da sola.</strong>",
    cz="<strong>SuperChain X™ maže a napíná řetěz sama.</strong>",
    es="<strong>SuperChain X™ lubrica y tensa sola.</strong>",
    hu="<strong>A SuperChain X™ magától ken és feszít.</strong>",
    pl="<strong>SuperChain X™ smaruje i napina sama.</strong>",
    pt="<strong>SuperChain X™ lubrifica e tensiona sozinha.</strong>",
)
add(
    "Olio sempre al posto giusto, tensione corretta, zero pause per regolare la catena.",
    cz="Olej vždy tam, kde má být, správné napnutí, žádné pauzy na seřízení řetězu.",
    es="Aceite siempre en su sitio, tensión correcta, cero pausas para ajustar la cadena.",
    hu="Az olaj mindig a helyén, a feszesség megfelelő, nincs megállás a lánc állításához.",
    pl="Olej zawsze tam, gdzie trzeba, właściwe napięcie, zero przerw na regulację łańcucha.",
    pt="Óleo sempre no sítio certo, tensão correta, zero pausas para regular a corrente.",
)
add(
    "<strong>4,9/5 — più di 8.730 giardini già sistemati.</strong>",
    cz="<strong>4,9/5 — více než 8 730 upravených zahrad.</strong>",
    es="<strong>4,9/5: más de 8.730 jardines ya puestos a punto.</strong>",
    hu="<strong>4,9/5 — több mint 8730 rendbe tett kert.</strong>",
    pl="<strong>4,9/5 — ponad 8730 uporządkowanych ogrodów.</strong>",
    pt="<strong>4,9/5 — mais de 8.730 jardins já arranjados.</strong>",
)
add(
    "Garanzia ufficiale 2 anni. 30 giorni per rese. Paghi solo quando arriva il corriere.",
    cz="Oficiální záruka 2 roky. 30 dní na vrácení. Platíte, až přijede kurýr.",
    es="Garantía oficial de 2 años. 30 días para devoluciones. Pagas solo cuando llega el repartidor.",
    hu="Hivatalos 2 év garancia. 30 napos visszaküldés. Csak akkor fizet, amikor a futár megérkezik.",
    pl="Oficjalna gwarancja 2 lata. 30 dni na zwrot. Płacisz dopiero, gdy przyjedzie kurier.",
    pt="Garantia oficial de 2 anos. 30 dias para devoluções. Paga só quando chega o estafeta.",
)
add(
    "Sì, voglio la Saw 7X™",
    cz="Ano, chci Saw 7X™",
    es="Sí, quiero la Saw 7X™",
    hu="Igen, kérem a Saw 7X™-et",
    pl="Tak, chcę Saw 7X™",
    pt="Sim, quero a Saw 7X™",
)
add(
    "💵 Paghi alla consegna",
    cz="💵 Platíte na dobírku",
    es="💵 Pagas al recibir",
    hu="💵 Fizetés átvételkor",
    pl="💵 Płacisz przy odbiorze",
    pt="💵 Paga na entrega",
)
add(
    "↩️ 30 giorni di prova",
    cz="↩️ 30 dní na vyzkoušení",
    es="↩️ 30 días de prueba",
    hu="↩️ 30 napos próba",
    pl="↩️ 30 dni na wypróbowanie",
    pt="↩️ 30 dias de teste",
)
add(
    "🚚 Spedizione gratuita",
    cz="🚚 Doprava zdarma",
    es="🚚 Envío gratis",
    hu="🚚 Ingyenes szállítás",
    pl="🚚 Darmowa dostawa",
    pt="🚚 Envio grátis",
)
add(
    "ACQUISTO SICURO • SPEDIZIONE GRATUITA • GARANZIA COMPLETA",
    cz="BEZPEČNÝ NÁKUP • DOPRAVA ZDARMA • PLNÁ ZÁRUKA",
    es="COMPRA SEGURA • ENVÍO GRATIS • GARANTÍA COMPLETA",
    hu="BIZTONSÁGOS VÁSÁRLÁS • INGYENES SZÁLLÍTÁS • TELJES GARANCIA",
    pl="BEZPIECZNY ZAKUP • DARMOWA DOSTAWA • PEŁNA GWARANCJA",
    pt="COMPRA SEGURA • ENVIO GRÁTIS • GARANTIA COMPLETA",
)
add(
    "<strong>Spedizione gratuita</strong><br>",
    cz="<strong>Doprava zdarma</strong><br>",
    es="<strong>Envío gratis</strong><br>",
    hu="<strong>Ingyenes szállítás</strong><br>",
    pl="<strong>Darmowa dostawa</strong><br>",
    pt="<strong>Envio grátis</strong><br>",
)
add(
    "<strong>Pagamento alla consegna</strong><br>",
    cz="<strong>Platba na dobírku</strong><br>",
    es="<strong>Pago contra reembolso</strong><br>",
    hu="<strong>Utánvétes fizetés</strong><br>",
    pl="<strong>Płatność przy odbiorze</strong><br>",
    pt="<strong>Pagamento na entrega</strong><br>",
)
add(
    "Niente carta e niente anticipo: paghi solo quando arriva il pacco",
    cz="Žádná karta a žádná záloha: platíte, až přijde balík",
    es="Sin tarjeta y sin adelanto: pagas solo cuando llega el paquete",
    hu="Nincs kártya és nincs előleg: akkor fizet, amikor a csomag megérkezik",
    pl="Bez karty i bez zaliczki: płacisz dopiero, gdy dotrze paczka",
    pt="Sem cartão e sem adiantamento: paga só quando chega a encomenda",
)
add(
    "<strong>Acquisto protetto</strong><br>",
    cz="<strong>Chráněný nákup</strong><br>",
    es="<strong>Compra protegida</strong><br>",
    hu="<strong>Védett vásárlás</strong><br>",
    pl="<strong>Zakup chroniony</strong><br>",
    pt="<strong>Compra protegida</strong><br>",
)
add(
    "I tuoi dati personali sono protetti al 100%",
    cz="Vaše osobní údaje jsou 100% chráněny",
    es="Tus datos personales están protegidos al 100%",
    hu="Személyes adatai 100%-ban védettek",
    pl="Twoje dane osobowe są chronione w 100%",
    pt="Os seus dados pessoais estão protegidos a 100%",
)
add(
    "<strong>Garanzia 2 anni</strong><br>",
    cz="<strong>Záruka 2 roky</strong><br>",
    es="<strong>Garantía de 2 años</strong><br>",
    hu="<strong>2 év garancia</strong><br>",
    pl="<strong>Gwarancja 2 lata</strong><br>",
    pt="<strong>Garantia de 2 anos</strong><br>",
)
add(
    "Puoi restituirlo senza pensieri entro 30 giorni",
    cz="Do 30 dnů ho můžete bez starostí vrátit",
    es="Puedes devolverlo sin complicaciones en 30 días",
    hu="Gond nélkül visszaküldheti 30 napon belül",
    pl="Możesz go zwrócić bez obaw w ciągu 30 dni",
    pt="Pode devolver sem preocupações em 30 dias",
)
add(
    "Disponibilità in magazzino",
    cz="Skladem",
    es="Disponibilidad en almacén",
    hu="Raktárkészlet",
    pl="Dostępność w magazynie",
    pt="Disponibilidade em armazém",
)
add(
    "RESTANO SOLO <span>4</span> KIT",
    cz="ZBÝVAJÍ JEN <span>4</span> SADY",
    es="QUEDAN SOLO <span>4</span> KITS",
    hu="MÁR CSAK <span>4</span> KÉSZLET",
    pl="ZOSTAŁY TYLKO <span>4</span> ZESTAWY",
    pt="RESTAM SÓ <span>4</span> KITS",
)
add("Importante!", cz="Důležité!", es="¡Importante!", hu="Fontos!", pl="Ważne!", pt="Importante!")
add(
    "Il magazzino si sta svuotando in fretta!",
    cz="Sklad se rychle vyprazdňuje!",
    es="¡El almacén se está vaciando rápido!",
    hu="A raktár gyorsan fogy!",
    pl="Magazyn szybko się opróżnia!",
    pt="O armazém está a esvaziar-se depressa!",
)
add(
    "In questo momento tante altre persone stanno guardando la Saw 7X™: per questo i kit disponibili scendono così in fretta.",
    cz="Právě teď si Saw 7X™ prohlíží spousta dalších lidí — proto sady mizí tak rychle.",
    es="Ahora mismo muchas otras personas están viendo la Saw 7X™: por eso los kits bajan tan rápido.",
    hu="Ebben a pillanatban sokan nézik a Saw 7X™-et: ezért fogynak ilyen gyorsan a készletek.",
    pl="W tej chwili wielu innych ogląda Saw 7X™: dlatego zestawy znikają tak szybko.",
    pt="Neste momento muitas outras pessoas estão a ver a Saw 7X™: por isso os kits descem tão depressa.",
)
add(
    "Ordina ora e assicurati uno degli ultimi kit al prezzo di oggi, con −50%.",
    cz="Objednejte teď a zajistěte si jednu z posledních sad za dnešní cenu se slevou −50 %.",
    es="Pide ahora y asegúrate uno de los últimos kits al precio de hoy, con −50%.",
    hu="Rendeljen most, és biztosítsa be az egyik utolsó készletet a mai áron, −50%-kal.",
    pl="Zamów teraz i zabezpiecz jeden z ostatnich zestawów w dzisiejszej cenie, z −50%.",
    pt="Encomende agora e garanta um dos últimos kits ao preço de hoje, com −50%.",
)
add(
    "Compila i tre campi. Ti chiamiamo entro 24 ore per confermare l’ordine e fissare la consegna. Paghi solo quando arriva il corriere.",
    cz="Vyplňte tři pole. Do 24 hodin zavoláme, potvrdíme objednávku a domluvíme doručení. Platíte, až přijede kurýr.",
    es="Rellena los tres campos. Te llamamos en 24 horas para confirmar el pedido y fijar la entrega. Pagas solo cuando llega el repartidor.",
    hu="Töltse ki a három mezőt. 24 órán belül felhívjuk a rendelés megerősítéséhez és a szállítás egyeztetéséhez. Csak a futár megérkezésekor fizet.",
    pl="Wypełnij trzy pola. Zadzwonimy w 24 godziny, by potwierdzić zamówienie i ustalić dostawę. Płacisz dopiero, gdy przyjedzie kurier.",
    pt="Preencha os três campos. Ligamos em 24 horas para confirmar a encomenda e marcar a entrega. Paga só quando chega o estafeta.",
)
add("Nome e Cognome*", cz="Jméno a příjmení*", es="Nombre y apellidos*", hu="Név*", pl="Imię i nazwisko*", pt="Nome e apelido*")
add("Telefono*", cz="Telefon*", es="Teléfono*", hu="Telefon*", pl="Telefon*", pt="Telefone*")
add(
    "Indirizzo di consegna*",
    cz="Doručovací adresa*",
    es="Dirección de entrega*",
    hu="Szállítási cím*",
    pl="Adres dostawy*",
    pt="Morada de entrega*",
)
add("CONFERMA ORDINE", cz="POTVRDIT OBJEDNÁVKU", es="CONFIRMAR PEDIDO", hu="RENDELÉS MEGERŐSÍTÉSE", pl="POTWIERDŹ ZAMÓWIENIE", pt="CONFIRMAR ENCOMENDA")
add(
    "Prenota la Saw 7X™ ",
    cz="Rezervujte Saw 7X™ ",
    es="Reserva la Saw 7X™ ",
    hu="Foglalja le a Saw 7X™-et ",
    pl="Zarezerwuj Saw 7X™ ",
    pt="Reserve a Saw 7X™ ",
)
add(
    "🔒 Nessun anticipo · Niente carta · Paghi solo alla consegna",
    cz="🔒 Žádná záloha · Bez karty · Platíte až při doručení",
    es="🔒 Sin adelanto · Sin tarjeta · Pagas solo al recibir",
    hu="🔒 Nincs előleg · Nincs kártya · Csak átvételkor fizet",
    pl="🔒 Bez zaliczki · Bez karty · Płacisz tylko przy odbiorze",
    pt="🔒 Sem adiantamento · Sem cartão · Paga só na entrega",
)
add(
    "Quante volte sei già salito su una scala instabile solo per tagliare un ramo?",
    cz="Kolikrát jste už lezli na vratký žebřík jen kvůli jedné větvi?",
    es="¿Cuántas veces has subido ya a una escalera inestable solo para cortar una rama?",
    hu="Hányszor mászott már instabil létrára csak azért, hogy levágjon egy ágat?",
    pl="Ile razy wchodziłeś już na chwiejną drabinę, tylko żeby obciąć gałąź?",
    pt="Quantas vezes já subiu a uma escada instável só para cortar um ramo?",
)
add(
    "Scala instabile e motosega a benzina: il rischio di ogni potatura",
    cz="Vratký žebřík a benzinová pila: riziko každého řezu",
    es="Escalera inestable y motosierra de gasolina: el riesgo de cada poda",
    hu="Instabil létra és benzines láncfűrész: minden metszés kockázata",
    pl="Chwiejna drabina i pilarka spalinowa: ryzyko każdego cięcia",
    pt="Escada instável e motosserra a gasolina: o risco de cada poda",
)
add(
    "Conosci la storia. La motosega a benzina fa un rumore assurdo, puzza di carburante e pesa 4 o 5 kg. Quella economica a batteria si blocca al primo tronco grosso. E per arrivare in cima all’albero da frutto… di nuovo la scala.",
    cz="Tu historii znáte. Benzinová pila řve, páchne palivem a váží 4–5 kg. Levná aku se zasekne u prvního silného kmene. A na vrchol ovocného stromu… zase žebřík.",
    es="Ya conoces la historia. La motosierra de gasolina hace un ruido absurdo, huele a combustible y pesa 4 o 5 kg. La barata de batería se atasca en el primer tronco grueso. Y para llegar a la copa del frutal… otra vez la escalera.",
    hu="Ismerős a történet. A benzines láncfűrész iszonyúan hangos, üzemanyagot szaglik, és 4–5 kg. Az olcsó akkumulátoros az első vastag törzsnél elakad. A gyümölcsfa tetejéhez… megint a létra.",
    pl="Znasz tę historię. Pilarka spalinowa hałasuje niemożliwie, śmierdzi paliwem i waży 4–5 kg. Tania akumulatorowa zacina się na pierwszym grubym pniu. A żeby dosięgnąć czubka drzewa owocowego… znowu drabina.",
    pt="Já conhece a história. A motosserra a gasolina faz um barulho absurdo, cheira a combustível e pesa 4 ou 5 kg. A barata a bateria trava no primeiro tronco grosso. E para chegar ao cimo da árvore de fruto… outra vez a escada.",
)
add(
    "<strong>Allora ne compri un’altra. E il ciclo ricomincia.</strong>",
    cz="<strong>Tak koupíte další. A cyklus začíná znovu.</strong>",
    es="<strong>Entonces compras otra. Y el ciclo vuelve a empezar.</strong>",
    hu="<strong>Aztán vesz egy másikat. És a kör kezdődik elölről.</strong>",
    pl="<strong>Więc kupujesz następną. I cykl zaczyna się od nowa.</strong>",
    pt="<strong>Então compra outra. E o ciclo recomeça.</strong>",
)
add(
    "Nemmeno la versione a benzina ti salva: rumore, fumi, miscela, cavo di avviamento. Ogni potatura diventa una mattinata intera — e un rischio inutile in cima alla scala.",
    cz="Ani benzinová verze vás nespasí: hluk, zplodiny, směs, startovací šňůra. Každý řez je celé dopoledne — a zbytečné riziko na vrcholu žebříku.",
    es="Ni la versión de gasolina te salva: ruido, humos, mezcla, cuerda de arranque. Cada poda se convierte en toda una mañana — y un riesgo inútil arriba de la escalera.",
    hu="A benzines verzió sem ment meg: zaj, füst, keverék, indítózsinór. Minden metszés egy fél nap — és felesleges kockázat a létra tetején.",
    pl="Nawet spalinowa wersja nie ratuje: hałas, spaliny, mieszanka, linka rozrusznika. Każde cięcie to całe przedpołudnie — i zbędne ryzyko na szczycie drabiny.",
    pt="Nem a versão a gasolina o salva: barulho, fumos, mistura, corda de arranque. Cada poda vira uma manhã inteira — e um risco inútil no cimo da escada.",
)
add(
    "Non è sfortuna.<br>",
    cz="Není to smůla.<br>",
    es="No es mala suerte.<br>",
    hu="Ez nem balszerencse.<br>",
    pl="To nie pech.<br>",
    pt="Não é azar.<br>",
)
add(
    "<strong>La verità è che la motosega tradizionale è nata per il suolo, non per la cima dell’albero — e quelle da pochi euro nascono per essere ricomprate.</strong>",
    cz="<strong>Pravda je, že klasická pila vznikla pro práci na zemi, ne v koruně stromu — a ty za pár korun se rodí k opětovnému nákupu.</strong>",
    es="<strong>La verdad es que la motosierra tradicional nació para el suelo, no para la copa del árbol — y las baratas nacen para que las vuelvas a comprar.</strong>",
    hu="<strong>Az igazság: a hagyományos láncfűrész a talajra készült, nem a fa tetejére — a filléres modellek pedig arra, hogy újra megvegye.</strong>",
    pl="<strong>Prawda jest taka, że tradycyjna pilarka powstała do pracy przy ziemi, nie w koronie drzewa — a te za parę złotych rodzą się po to, by kupować je ponownie.</strong>",
    pt="<strong>A verdade é que a motosserra tradicional nasceu para o chão, não para o cimo da árvore — e as baratas nascem para serem compradas outra vez.</strong>",
)
add(
    "La manutenzione che non devi più fare",
    cz="Údržba, kterou už nemusíte dělat",
    es="El mantenimiento que ya no tienes que hacer",
    hu="A karbantartás, amit többé nem kell végeznie",
    pl="Konserwacja, której już nie musisz robić",
    pt="A manutenção que já não precisa de fazer",
)
add(
    "SuperChain X™ cambia le regole della catena",
    cz="SuperChain X™ mění pravidla řetězu",
    es="SuperChain X™ cambia las reglas de la cadena",
    hu="A SuperChain X™ újraszabja a lánc szabályait",
    pl="SuperChain X™ zmienia zasady łańcucha",
    pt="SuperChain X™ muda as regras da corrente",
)
add(
    "Lubrificazione automatica della catena Saw 7X™",
    cz="Automatické mazání řetězu Saw 7X™",
    es="Lubricación automática de la cadena Saw 7X™",
    hu="A Saw 7X™ láncának automatikus kenése",
    pl="Automatyczne smarowanie łańcucha Saw 7X™",
    pt="Lubrificação automática da corrente Saw 7X™",
)
add(
    "Con una motosega tradizionale passi il tempo a lubrificare e a tendere la catena. Senza olio, si surriscalda. Senza tensione, salta o si blocca. E il taglio si ferma a metà ramo.",
    cz="S klasickou pilou trávíte čas mazáním a napínáním řetězu. Bez oleje se přehřeje. Bez napnutí přeskočí nebo se zasekne. A řez skončí v polovině větve.",
    es="Con una motosierra tradicional pasas el tiempo lubricando y tensando la cadena. Sin aceite, se calienta. Sin tensión, salta o se atasca. Y el corte se para a mitad de rama.",
    hu="Hagyományos láncfűrésszel az idő a kenéssel és feszítéssel megy el. Olaj nélkül túlmelegszik. Feszesség nélkül ugrik vagy beragad. A vágás az ág közepén megáll.",
    pl="Przy tradycyjnej pilarce czas schodzi na smarowanie i napinanie łańcucha. Bez oleju się przegrzewa. Bez napięcia zeskakuje albo zacina. I cięcie staje w połowie gałęzi.",
    pt="Com uma motosserra tradicional passa o tempo a lubrificar e a tensionar a corrente. Sem óleo, sobreaquece. Sem tensão, salta ou trava. E o corte pára a meio do ramo.",
)
add(
    "Il sistema distribuisce l’olio senza sosta e tiene la tensione giusta. Le prestazioni restano stabili dal primo all’ultimo taglio.",
    cz="Systém olej dávkuje bez přestání a drží správné napnutí. Výkon zůstává stabilní od prvního do posledního řezu.",
    es="El sistema reparte el aceite sin parar y mantiene la tensión correcta. El rendimiento se mantiene estable del primer al último corte.",
    hu="A rendszer folyamatosan adagolja az olajat és tartja a megfelelő feszességet. A teljesítmény az első vágástól az utolsóig stabil marad.",
    pl="System podaje olej bez przerwy i trzyma właściwe napięcie. Wydajność zostaje stabilna od pierwszego do ostatniego cięcia.",
    pt="O sistema distribui o óleo sem parar e mantém a tensão certa. O desempenho fica estável do primeiro ao último corte.",
)
add(
    "<strong>È esattamente il sistema montato sulla Saw 7X™.</strong>",
    cz="<strong>Přesně tento systém je v Saw 7X™.</strong>",
    es="<strong>Es exactamente el sistema montado en la Saw 7X™.</strong>",
    hu="<strong>Pontosan ez a rendszer van a Saw 7X™-ben.</strong>",
    pl="<strong>To dokładnie ten system zamontowany w Saw 7X™.</strong>",
    pt="<strong>É exatamente o sistema montado na Saw 7X™.</strong>",
)
add(
    "Per questo continui a tagliare senza pause e senza regolazioni ogni dieci minuti.",
    cz="Proto řežete bez pauz a bez seřizování každých deset minut.",
    es="Por eso sigues cortando sin pausas y sin ajustes cada diez minutos.",
    hu="Ezért vághat tovább megállás és tízpercenkénti állítás nélkül.",
    pl="Dlatego tniesz bez przerw i bez regulacji co dziesięć minut.",
    pt="Por isso continua a cortar sem pausas e sem afinações a cada dez minutos.",
)
add(
    "È lo stesso ragionamento che separa un attrezzo che chiede attenzione continua da uno che semplicemente lavora: meno regolazioni, più taglio, meno manutenzione.",
    cz="Stejný rozdíl je mezi nářadím, které chce neustálou péči, a tím, které prostě pracuje: méně seřizování, více řezání, méně údržby.",
    es="Es el mismo razonamiento que separa una herramienta que pide atención continua de una que simplemente trabaja: menos ajustes, más corte, menos mantenimiento.",
    hu="Ugyanaz a különbség, mint a folyamatos figyelmet igénylő és az egyszerűen dolgozó szerszám között: kevesebb állítás, több vágás, kevesebb karbantartás.",
    pl="To ta sama logika, która oddziela narzędzie wymagające ciągłej uwagi od takiego, które po prostu działa: mniej regulacji, więcej cięcia, mniej konserwacji.",
    pt="É o mesmo raciocínio que separa uma ferramenta que pede atenção contínua de uma que simplesmente trabalha: menos afinações, mais corte, menos manutenção.",
)
add(
    "Qui non è pubblicità. <b>È il sistema che fa il lavoro.</b>",
    cz="Tady nejde o reklamu. <b>Je to systém, který odvádí práci.</b>",
    es="Aquí no es publicidad. <b>Es el sistema que hace el trabajo.</b>",
    hu="Ez nem reklám. <b>Ez a rendszer végzi a munkát.</b>",
    pl="Tu nie ma reklamy. <b>To system, który wykonuje robotę.</b>",
    pt="Aqui não é publicidade. <b>É o sistema que faz o trabalho.</b>",
)
add(
    "✅ I vantaggi concreti",
    cz="✅ Konkrétní výhody",
    es="✅ Las ventajas concretas",
    hu="✅ Konkrét előnyök",
    pl="✅ Konkretne zalety",
    pt="✅ As vantagens concretas",
)
add(
    "Questa è la motosega che ti toglie la scala dal giardino",
    cz="Tohle je pila, která vám ze zahrady vezme žebřík",
    es="Esta es la motosierra que te quita la escalera del jardín",
    hu="Ez az a láncfűrész, amely kiveszi a létrát a kertből",
    pl="To pilarka, która zabiera drabinę z ogrodu",
    pt="Esta é a motosserra que lhe tira a escada do jardim",
)
add(
    "Più potenza sui rami grossi, zero benzina, meno peso sulle braccia. E il giardino torna in ordine in un solo giorno.",
    cz="Více síly na silné větve, žádný benzín, méně váhy na rukou. A zahrada je za jeden den v pořádku.",
    es="Más potencia en las ramas gruesas, cero gasolina, menos peso en los brazos. Y el jardín vuelve a estar en orden en un solo día.",
    hu="Több erő a vastag ágakon, nulla benzin, kevesebb súly a karokon. És a kert egy nap alatt rendbe jön.",
    pl="Więcej mocy na grubych gałęziach, zero benzyny, mniej ciężaru na ramionach. A ogród wraca do porządku w jeden dzień.",
    pt="Mais potência nos ramos grossos, zero gasolina, menos peso nos braços. E o jardim volta a estar em ordem num só dia.",
)
add(
    "Saw 7X™ con asta telescopica fino a 5 metri",
    cz="Saw 7X™ s teleskopickou tyčí až 5 metrů",
    es="Saw 7X™ con pértiga telescópica de hasta 5 metros",
    hu="Saw 7X™ teleszkópos rúddal akár 5 méterig",
    pl="Saw 7X™ z wysięgnikiem teleskopowym do 5 metrów",
    pt="Saw 7X™ com haste telescópica até 5 metros",
)
add(
    "3.000 W e 5 metri — la cima dell’albero smette di essere un problema",
    cz="3 000 W a 5 metrů — vrchol stromu přestává být problém",
    es="3.000 W y 5 metros: la copa del árbol deja de ser un problema",
    hu="3000 W és 5 méter — a fa teteje többé nem gond",
    pl="3000 W i 5 metrów — czubek drzewa przestaje być problemem",
    pt="3.000 W e 5 metros — o cimo da árvore deixa de ser um problema",
)
add(
    "Dove un decespugliatore normale si ferma, la Saw 7X™ continua. La lama attraversa legno verde e secco, rami grossi e tronchi fino a 35 cm. Vicino al suolo usi il modo manuale compatto. In cima, monti l’asta telescopica.",
    cz="Tam, kde se běžný křovinořez zastaví, Saw 7X™ pokračuje. Čepel projde zeleným i suchým dřevem, silnými větvemi i kmeny až do 35 cm. U země použijete kompaktní ruční režim. Nahoře nasadíte teleskopickou tyč.",
    es="Donde una desbrozadora normal se detiene, la Saw 7X™ sigue. La hoja atraviesa madera verde y seca, ramas gruesas y troncos de hasta 35 cm. Cerca del suelo usas el modo manual compacto. Arriba, montas la pértiga telescópica.",
    hu="Ahol egy sima fűkasza megáll, a Saw 7X™ folytatja. A lánc átmegy zöld és száraz fán, vastag ágakon és akár 35 cm-es törzseken. A talaj közelében a kompakt kézi módot használja. Fent felteszi a teleszkópos rudat.",
    pl="Tam, gdzie zwykła wykaszarka się zatrzymuje, Saw 7X™ idzie dalej. Ostrze przecina zielone i suche drewno, grube gałęzie i pnie do 35 cm. Przy ziemi używasz trybu ręcznego. Na górze montujesz wysięgnik teleskopowy.",
    pt="Onde um corta-mato normal pára, a Saw 7X™ continua. A lâmina atravessa madeira verde e seca, ramos grossos e troncos até 35 cm. Perto do chão usa o modo manual compacto. No cimo, monta a haste telescópica.",
)
add(
    "Taglio da 35 cm. Potenza da 3.000 W. Altezza fino a 5 metri.",
    cz="Řez 35 cm. Výkon 3 000 W. Výška až 5 metrů.",
    es="Corte de 35 cm. Potencia de 3.000 W. Altura hasta 5 metros.",
    hu="35 cm-es vágás. 3000 W teljesítmény. Magasság akár 5 méter.",
    pl="Cięcie 35 cm. Moc 3000 W. Wysokość do 5 metrów.",
    pt="Corte de 35 cm. Potência de 3.000 W. Altura até 5 metros.",
)
add(
    "I lavori più pesanti stanno in un solo giorno.",
    cz="Nejtěžší práce zvládnete za jeden den.",
    es="Los trabajos más duros caben en un solo día.",
    hu="A legnehezebb munka is belefér egy napba.",
    pl="Najcięższe prace mieszczą się w jednym dniu.",
    pt="Os trabalhos mais pesados cabem num só dia.",
)
add(
    "Saw 7X™ a batteria che taglia un tronco senza cavi",
    cz="Aku Saw 7X™ řeže kmen bez kabelů",
    es="Saw 7X™ a batería cortando un tronco sin cables",
    hu="Akkumulátoros Saw 7X™ kábel nélkül vágja a törzset",
    pl="Akumulatorowa Saw 7X™ tnie pień bez kabli",
    pt="Saw 7X™ a bateria a cortar um tronco sem cabos",
)
add(
    "Due batterie da 48 V. Senza benzina e senza cavi",
    cz="Dvě baterie 48 V. Bez benzínu a bez kabelů",
    es="Dos baterías de 48 V. Sin gasolina y sin cables",
    hu="Két 48 V-os akkumulátor. Benzin és kábel nélkül",
    pl="Dwa akumulatory 48 V. Bez benzyny i bez kabli",
    pt="Duas baterias de 48 V. Sem gasolina e sem cabos",
)
add(
    "Dimentica benzina, miscela e prolunghe che limitano i movimenti e si avvolgono ai piedi. Quando una batteria finisce, metti la seconda e vai avanti. Ricarica in 45 minuti.",
    cz="Zapomeňte na benzín, směs a prodlužováky, které omezují pohyb a pletou se pod nohama. Až jedna baterie dojde, dáte druhou a pokračujete. Nabití za 45 minut.",
    es="Olvida gasolina, mezcla y alargadores que limitan el movimiento y se enredan en los pies. Cuando una batería se acaba, pones la segunda y sigues. Recarga en 45 minutos.",
    hu="Felejtse el a benzint, a keveréket és a mozgást korlátozó, lábába tekeredő hosszabbítókat. Ha az egyik akku lemerül, beteszi a másodikat és megy tovább. Töltés 45 perc.",
    pl="Zapomnij o benzynie, mieszance i przedłużaczach, które ograniczają ruchy i plączą się pod nogami. Gdy jeden akumulator się skończy, wkładasz drugi i jedziesz dalej. Ładowanie w 45 minut.",
    pt="Esqueça gasolina, mistura e extensões que limitam os movimentos e se enrolam nos pés. Quando uma bateria acaba, põe a segunda e segue. Carregamento em 45 minutos.",
)
add(
    "48 V · 8.000 mAh · senza fili · carica in 45 min.",
    cz="48 V · 8 000 mAh · bez kabelu · nabití za 45 min.",
    es="48 V · 8.000 mAh · sin cables · carga en 45 min.",
    hu="48 V · 8000 mAh · vezeték nélkül · töltés 45 perc.",
    pl="48 V · 8000 mAh · bezprzewodowo · ładowanie w 45 min.",
    pt="48 V · 8.000 mAh · sem fios · carga em 45 min.",
)
add(
    "Ti muovi in tutta la proprietà senza dipendere da una presa.",
    cz="Pohybujete se po celém pozemku bez závislosti na zásuvce.",
    es="Te mueves por toda la finca sin depender de un enchufe.",
    hu="Az egész telken mozoghat konnektor nélkül.",
    pl="Poruszasz się po całej posesji bez gniazdka.",
    pt="Move-se por toda a propriedade sem depender de uma tomada.",
)
add(
    "Saw 7X™ in una mano: 700 g, 48 V",
    cz="Saw 7X™ v jedné ruce: 700 g, 48 V",
    es="Saw 7X™ en una mano: 700 g, 48 V",
    hu="Saw 7X™ egy kézben: 700 g, 48 V",
    pl="Saw 7X™ w jednej ręce: 700 g, 48 V",
    pt="Saw 7X™ numa mão: 700 g, 48 V",
)
add(
    "700 g. La controlli con una mano, senza distruggerti la schiena",
    cz="700 g. Ovládáte ji jednou rukou, bez zničených zad",
    es="700 g. La controlas con una mano, sin destrozarte la espalda",
    hu="700 g. Egy kézzel irányítja, a hátának kímélésével",
    pl="700 g. Sterujesz jedną ręką, bez rujnowania pleców",
    pt="700 g. Controla-a com uma mão, sem estragar as costas",
)
add(
    "Una motosega tradizionale pesa 4–5 kg. La Saw 7X™ pesa 700 g e riduce la fatica di braccia, spalle e schiena, anche nei lavori più lunghi. Il corpo compatto entra negli spazi stretti. Freno istantaneo.",
    cz="Klasická pila váží 4–5 kg. Saw 7X™ váží 700 g a snižuje námahu paží, ramen i zad i při delší práci. Kompaktní tělo se vejde do úzkých míst. Okamžitá brzda.",
    es="Una motosierra tradicional pesa 4–5 kg. La Saw 7X™ pesa 700 g y reduce el cansancio de brazos, hombros y espalda, también en los trabajos más largos. El cuerpo compacto entra en huecos estrechos. Freno instantáneo.",
    hu="Egy hagyományos láncfűrész 4–5 kg. A Saw 7X™ 700 g, és csökkenti a kar, a váll és a hát terhelését hosszabb munkánál is. A kompakt test befér a szűk helyekre. Azonnali fék.",
    pl="Tradycyjna pilarka waży 4–5 kg. Saw 7X™ waży 700 g i zmniejsza zmęczenie ramion, barków i pleców, także przy dłuższej pracy. Kompaktowy korpus wchodzi w ciasne miejsca. Natychmiastowy hamulec.",
    pt="Uma motosserra tradicional pesa 4–5 kg. A Saw 7X™ pesa 700 g e reduz o cansaço de braços, ombros e costas, mesmo nos trabalhos mais longos. O corpo compacto entra em espaços estreitos. Travão instantâneo.",
)
add(
    "700 g · una mano · freno istantaneo.",
    cz="700 g · jedna ruka · okamžitá brzda.",
    es="700 g · una mano · freno instantáneo.",
    hu="700 g · egy kéz · azonnali fék.",
    pl="700 g · jedna ręka · natychmiastowy hamulec.",
    pt="700 g · uma mão · travão instantâneo.",
)
add(
    "Tagli con precisione dove l’attrezzo pesante non arriva nemmeno.",
    cz="Řežete přesně tam, kam těžké nářadí ani nedosáhne.",
    es="Cortas con precisión donde la herramienta pesada ni siquiera llega.",
    hu="Pontosan vág ott, ahová a nehéz szerszám el sem ér.",
    pl="Tniesz precyzyjnie tam, gdzie ciężkie narzędzie nawet nie dosięga.",
    pt="Corta com precisão onde a ferramenta pesada nem chega.",
)
add(
    "💵 Paghi quando arriva",
    cz="💵 Platíte, až to dorazí",
    es="💵 Pagas cuando llega",
    hu="💵 Akkor fizet, amikor megérkezik",
    pl="💵 Płacisz, gdy dotrze",
    pt="💵 Paga quando chega",
)
add(
    "🚚 Consegna in 24/48h",
    cz="🚚 Doručení do 24/48h",
    es="🚚 Entrega en 24/48h",
    hu="🚚 Kézbesítés 24/48 óra",
    pl="🚚 Dostawa w 24/48h",
    pt="🚚 Entrega em 24/48h",
)
add(
    "↩️ Provalo 30 giorni",
    cz="↩️ Vyzkoušejte 30 dní",
    es="↩️ Pruébalo 30 días",
    hu="↩️ Próbálja 30 napig",
    pl="↩️ Wypróbuj 30 dni",
    pt="↩️ Experimente 30 dias",
)
add(
    "Confronto senza filtri",
    cz="Srovnání bez příkras",
    es="Comparación sin filtros",
    hu="Szűretlen összehasonlítás",
    pl="Porównanie bez filtrów",
    pt="Comparação sem filtros",
)
add(
    "Motosega tradizionale o Saw 7X™?",
    cz="Klasická pila, nebo Saw 7X™?",
    es="¿Motosierra tradicional o Saw 7X™?",
    hu="Hagyományos láncfűrész vagy Saw 7X™?",
    pl="Tradycyjna pilarka czy Saw 7X™?",
    pt="Motosserra tradicional ou Saw 7X™?",
)
add(
    "Gli stessi criteri. Senza fronzoli.",
    cz="Stejná kritéria. Bez zbytečností.",
    es="Los mismos criterios. Sin adornos.",
    hu="Ugyanazok a szempontok. Cifrázás nélkül.",
    pl="Te same kryteria. Bez ozdobników.",
    pt="Os mesmos critérios. Sem enfeites.",
)
add("Tradizionale", cz="Klasická", es="Tradicional", hu="Hagyományos", pl="Tradycyjna", pt="Tradicional")
add(
    "⛽ Benzina, rumore e fumi",
    cz="⛽ Benzín, hluk a zplodiny",
    es="⛽ Gasolina, ruido y humos",
    hu="⛽ Benzin, zaj és füst",
    pl="⛽ Benzyna, hałas i spaliny",
    pt="⛽ Gasolina, barulho e fumos",
)
add(
    "Batteria, senza benzina",
    cz="Baterie, bez benzínu",
    es="Batería, sin gasolina",
    hu="Akkumulátor, benzin nélkül",
    pl="Akumulator, bez benzyny",
    pt="Bateria, sem gasolina",
)
add("🏋️ 4–5 kg", cz="🏋️ 4–5 kg", es="🏋️ 4–5 kg", hu="🏋️ 4–5 kg", pl="🏋️ 4–5 kg", pt="🏋️ 4–5 kg")
add("Solo 700 g", cz="Jen 700 g", es="Solo 700 g", hu="Csak 700 g", pl="Tylko 700 g", pt="Só 700 g")
add(
    "🪜 Ti serve una scala",
    cz="🪜 Potřebujete žebřík",
    es="🪜 Necesitas una escalera",
    hu="🪜 Létra kell hozzá",
    pl="🪜 Potrzebujesz drabiny",
    pt="🪜 Precisa de uma escada",
)
add(
    "Asta fino a 5 metri",
    cz="Tyč až 5 metrů",
    es="Pértiga hasta 5 metros",
    hu="Rúd akár 5 méter",
    pl="Wysięgnik do 5 metrów",
    pt="Haste até 5 metros",
)
add(
    "🔧 Regolazioni continue",
    cz="🔧 Neustálé seřizování",
    es="🔧 Ajustes continuos",
    hu="🔧 Folyamatos állítgatás",
    pl="🔧 Ciągłe regulacje",
    pt="🔧 Afinações contínuas",
)
add(
    "🛢️ Rifornimento di benzina",
    cz="🛢️ Tankování benzínu",
    es="🛢️ Repostar gasolina",
    hu="🛢️ Benzinutántöltés",
    pl="🛢️ Tankowanie benzyny",
    pt="🛢️ Abastecimento de gasolina",
)
add(
    "Due batterie da 48 V",
    cz="Dvě baterie 48 V",
    es="Dos baterías de 48 V",
    hu="Két 48 V-os akku",
    pl="Dwa akumulatory 48 V",
    pt="Duas baterias de 48 V",
)
add(
    "⭐ Più di 8.730 giardini",
    cz="⭐ Více než 8 730 zahrad",
    es="⭐ Más de 8.730 jardines",
    hu="⭐ Több mint 8730 kert",
    pl="⭐ Ponad 8730 ogrodów",
    pt="⭐ Mais de 8.730 jardins",
)
add(
    "Chi la prova non la molla più",
    cz="Kdo ji vyzkouší, už ji nepustí",
    es="Quien la prueba no la suelta",
    hu="Aki kipróbálja, nem engedi el",
    pl="Kto jej spróbuje, już nie odpuszcza",
    pt="Quem a experimenta já não larga",
)
add(
    "C’è chi lascia la benzina e chi ha già bruciato soldi su versioni economiche: è questo che li porta a scegliere la Saw 7X™.",
    cz="Někdo nechává benzín, někdo už spálil peníze na levných verzích: proto sahají po Saw 7X™.",
    es="Hay quien deja la gasolina y quien ya ha quemado dinero en versiones baratas: eso es lo que les lleva a elegir la Saw 7X™.",
    hu="Van, aki otthagyja a benzint, és van, aki olcsó verziókra költött: ezért választják a Saw 7X™-et.",
    pl="Jedni odchodzą od benzyny, inni spalili już pieniądze na tanich wersjach: dlatego wybierają Saw 7X™.",
    pt="Há quem deixe a gasolina e quem já queimou dinheiro em versões baratas: é isso que os leva a escolher a Saw 7X™.",
)
add(
    "Roberto G. — Saw 7X™ in uso",
    cz="Roberto G. — Saw 7X™ v akci",
    es="Roberto G. — Saw 7X™ en uso",
    hu="Roberto G. — Saw 7X™ munka közben",
    pl="Roberto G. — Saw 7X™ w użyciu",
    pt="Roberto G. — Saw 7X™ em uso",
)
add(
    "“La catena attraversa in fretta anche i rami secchi più grossi, senza fatica e senza bloccarsi. Pensavo di dover usare molta più forza, invece basta guidarla con una mano.”",
    cz="„Řetěz rychle projde i těmi nejsilnějšími suchými větvemi, bez dřiny a bez zasekávání. Čekal jsem, že budu muset víc tlačit, ale stačí ji vést jednou rukou.“",
    es="“La cadena atraviesa rápido incluso las ramas secas más gruesas, sin esfuerzo y sin atascarse. Pensaba que tendría que hacer mucha más fuerza, pero basta con guiarla con una mano.”",
    hu="„A lánc gyorsan átmegy a legvastagabb száraz ágakon is, erőlködés és beragadás nélkül. Azt hittem, sokkal több erőt kell használnom, de elég egy kézzel vezetni.”",
    pl="„Łańcuch szybko przechodzi nawet przez najgrubsze suche gałęzie, bez wysiłku i bez zacinania. Myślałem, że będę musiał użyć dużo więcej siły, a wystarczy prowadzić ją jedną ręką.”",
    pt="“A corrente atravessa depressa até os ramos secos mais grossos, sem esforço e sem travar. Pensava que ia precisar de muita mais força, mas basta guiá-la com uma mão.”",
)
add(
    "✅ Una potenza sorprendente",
    cz="✅ Překvapivý výkon",
    es="✅ Una potencia sorprendente",
    hu="✅ Meglepő erő",
    pl="✅ Zaskakująca moc",
    pt="✅ Uma potência surpreendente",
)
add(
    "David M. — Saw 7X™ in mano",
    cz="David M. — Saw 7X™ v ruce",
    es="David M. — Saw 7X™ en la mano",
    hu="David M. — Saw 7X™ a kézben",
    pl="David M. — Saw 7X™ w dłoni",
    pt="David M. — Saw 7X™ na mão",
)
add(
    "“È potente, comoda da tenere in mano e facile da usare, anche per chi non aveva mai preso una motosega. In un pomeriggio ho potato tutti gli alberi da frutto del giardino.”",
    cz="„Je silná, pohodlně se drží a snadno se používá, i když jste nikdy pilu v ruce neměli. Za odpoledne jsem ostříhal všechny ovocné stromy na zahradě.“",
    es="“Es potente, cómoda de sujetar y fácil de usar, también para quien nunca había cogido una motosierra. En una tarde podé todos los frutales del jardín.”",
    hu="„Erős, kényelmesen tartható és könnyen használható, akkor is, ha valaki még soha nem fogott láncfűrészt. Egy délután alatt megmetszettem a kert összes gyümölcsfáját.”",
    pl="„Jest mocna, wygodna w dłoni i łatwa w obsłudze, nawet dla kogoś, kto nigdy nie brał pilarki. W jedno popołudnie przyciąłem wszystkie drzewa owocowe w ogrodzie.”",
    pt="“É potente, confortável de segurar e fácil de usar, mesmo para quem nunca tinha pego numa motosserra. Numa tarde podei todas as árvores de fruto do jardim.”",
)
add(
    "✅ Fa il suo lavoro",
    cz="✅ Dělá, co má",
    es="✅ Hace su trabajo",
    hu="✅ Elvégzi a dolgát",
    pl="✅ Robi swoje",
    pt="✅ Faz o seu trabalho",
)
add(
    "Miguel T. — Saw 7X™ con asta telescopica",
    cz="Miguel T. — Saw 7X™ s teleskopickou tyčí",
    es="Miguel T. — Saw 7X™ con pértiga telescópica",
    hu="Miguel T. — Saw 7X™ teleszkópos rúddal",
    pl="Miguel T. — Saw 7X™ z wysięgnikiem teleskopowym",
    pt="Miguel T. — Saw 7X™ com haste telescópica",
)
add(
    "“L’asta telescopica arriva senza fatica ai rami più alti, quindi non devo più salire su una scala instabile. Ho finito in metà tempo e mi sono sentito molto più sicuro.”",
    cz="„Teleskopická tyč bez námahy dosáhne na nejvyšší větve, takže už nemusím na vratký žebřík. Skončil jsem v polovičním čase a cítil jsem se mnohem jistěji.“",
    es="“La pértiga telescópica llega sin esfuerzo a las ramas más altas, así que ya no tengo que subir a una escalera inestable. Terminé en la mitad de tiempo y me sentí mucho más seguro.”",
    hu="„A teleszkópos rúd erőlködés nélkül eléri a legmagasabb ágakat, így nem kell instabil létrára másznom. Fél idő alatt végeztem, és sokkal biztonságosabban éreztem magam.”",
    pl="„Wysięgnik teleskopowy bez wysiłku dosięga najwyższych gałęzi, więc nie muszę już wchodzić na chwiejną drabinę. Skończyłem w połowie czasu i czułem się znacznie pewniej.”",
    pt="“A haste telescópica chega sem esforço aos ramos mais altos, por isso já não tenho de subir a uma escada instável. Acabei em metade do tempo e senti-me muito mais seguro.”",
)
add(
    "✅ Più veloce e più sicura",
    cz="✅ Rychlejší a bezpečnější",
    es="✅ Más rápida y más segura",
    hu="✅ Gyorsabb és biztonságosabb",
    pl="✅ Szybsza i bezpieczniejsza",
    pt="✅ Mais rápida e mais segura",
)
add("📦 Tutto incluso", cz="📦 Vše v sadě", es="📦 Todo incluido", hu="📦 Minden benne van", pl="📦 Wszystko w zestawie", pt="📦 Tudo incluído")
add(
    "Kit completo Saw 7X™.<br>",
    cz="Kompletní sada Saw 7X™.<br>",
    es="Kit completo Saw 7X™.<br>",
    hu="Teljes Saw 7X™ készlet.<br>",
    pl="Kompletny zestaw Saw 7X™.<br>",
    pt="Kit completo Saw 7X™.<br>",
)
add(
    "Niente extra. Niente sorprese.",
    cz="Nic navíc. Žádná překvapení.",
    es="Nada extra. Sin sorpresas.",
    hu="Nincs felár. Nincs meglepetés.",
    pl="Nic extra. Żadnych niespodzianek.",
    pt="Nada extra. Sem surpresas.",
)
add(
    "Apri la scatola, monti e inizi a tagliare. Non manca niente.",
    cz="Otevřete krabici, sestavíte a začnete řezat. Nic nechybí.",
    es="Abres la caja, montas y empiezas a cortar. No falta nada.",
    hu="Kinyitja a dobozt, összeszereli és vágni kezd. Semmi sem hiányzik.",
    pl="Otwierasz pudełko, składasz i zaczynasz ciąć. Nic nie brakuje.",
    pt="Abre a caixa, monta e começa a cortar. Não falta nada.",
)
add(
    "Kit completo Saw 7X™ — tutto quello che c’è nel pacco",
    cz="Kompletní sada Saw 7X™ — vše, co je v balení",
    es="Kit completo Saw 7X™: todo lo que hay en el paquete",
    hu="Teljes Saw 7X™ készlet — minden, ami a csomagban van",
    pl="Kompletny zestaw Saw 7X™ — wszystko, co jest w paczce",
    pt="Kit completo Saw 7X™ — tudo o que está na encomenda",
)
add(
    "Cosa c’è nella scatola",
    cz="Co je v krabici",
    es="Qué hay en la caja",
    hu="Mi van a dobozban",
    pl="Co jest w pudełku",
    pt="O que está na caixa",
)
add(
    "A cosa serve davvero",
    cz="K čemu to opravdu je",
    es="Para qué sirve de verdad",
    hu="Mire való valójában",
    pl="Do czego naprawdę służy",
    pt="Para que serve de verdade",
)
add(
    "⚙️ Motosega elettrica Saw 7X™",
    cz="⚙️ Elektrická pila Saw 7X™",
    es="⚙️ Motosierra eléctrica Saw 7X™",
    hu="⚙️ Elektromos láncfűrész Saw 7X™",
    pl="⚙️ Elektryczna pilarka Saw 7X™",
    pt="⚙️ Motosserra elétrica Saw 7X™",
)
add(
    "3.000 W in modalità compatta — il cuore del kit",
    cz="3 000 W v kompaktním režimu — srdce sady",
    es="3.000 W en modo compacto: el corazón del kit",
    hu="3000 W kompakt módban — a készlet szíve",
    pl="3000 W w trybie kompaktowym — serce zestawu",
    pt="3.000 W em modo compacto — o coração do kit",
)
add(
    "🪜 Asta telescopica fino a 5 metri",
    cz="🪜 Teleskopická tyč až 5 metrů",
    es="🪜 Pértiga telescópica de hasta 5 metros",
    hu="🪜 Teleszkópos rúd akár 5 méterig",
    pl="🪜 Wysięgnik teleskopowy do 5 metrów",
    pt="🪜 Haste telescópica até 5 metros",
)
add(
    "Arrivi in cima all’albero senza scala",
    cz="Na vrchol stromu bez žebříku",
    es="Llegas a la copa del árbol sin escalera",
    hu="Eléri a fa tetejét létra nélkül",
    pl="Sięgasz czubka drzewa bez drabiny",
    pt="Chega ao cimo da árvore sem escada",
)
add(
    "🔋 2 batterie da 48 V e 8.000 mAh",
    cz="🔋 2 baterie 48 V a 8 000 mAh",
    es="🔋 2 baterías de 48 V y 8.000 mAh",
    hu="🔋 2 darab 48 V-os, 8000 mAh-s akku",
    pl="🔋 2 akumulatory 48 V i 8000 mAh",
    pt="🔋 2 baterias de 48 V e 8.000 mAh",
)
add(
    "Una al lavoro, l’altra in carica — non ti fermi",
    cz="Jedna pracuje, druhá se nabíjí — nezastavíte se",
    es="Una trabaja, la otra carga: no te paras",
    hu="Az egyik dolgozik, a másik tölt — nem áll meg",
    pl="Jeden pracuje, drugi się ładuje — nie stajesz",
    pt="Uma a trabalhar, a outra a carregar — não pára",
)
add(
    "⚡ Caricabatterie rapido",
    cz="⚡ Rychlonabíječka",
    es="⚡ Cargador rápido",
    hu="⚡ Gyors töltő",
    pl="⚡ Szybka ładowarka",
    pt="⚡ Carregador rápido",
)
add(
    "45 minuti e torni a tagliare",
    cz="45 minut a zase řežete",
    es="45 minutos y vuelves a cortar",
    hu="45 perc, és újra vághat",
    pl="45 minut i wracasz do cięcia",
    pt="45 minutos e volta a cortar",
)
add(
    "⛓️ 2 catene di ricambio",
    cz="⛓️ 2 náhradní řetězy",
    es="⛓️ 2 cadenas de recambio",
    hu="⛓️ 2 tartalék lánc",
    pl="⛓️ 2 łańcuchy zapasowe",
    pt="⛓️ 2 correntes de substituição",
)
add(
    "Non resti a metà ramo senza catena",
    cz="Nezůstanete v polovině větve bez řetězu",
    es="No te quedas a mitad de rama sin cadena",
    hu="Nem marad ág közepén lánc nélkül",
    pl="Nie zostajesz w połowie gałęzi bez łańcucha",
    pt="Não fica a meio do ramo sem corrente",
)
add(
    "🛢️ Serbatoio olio + SuperChain X™",
    cz="🛢️ Nádržka na olej + SuperChain X™",
    es="🛢️ Depósito de aceite + SuperChain X™",
    hu="🛢️ Olajtartály + SuperChain X™",
    pl="🛢️ Zbiornik oleju + SuperChain X™",
    pt="🛢️ Depósito de óleo + SuperChain X™",
)
add(
    "Lubrifica e tende da sola — manutenzione minima",
    cz="Maže a napíná sama — minimální údržba",
    es="Lubrica y tensa sola: mantenimiento mínimo",
    hu="Magától ken és feszít — minimális karbantartás",
    pl="Smaruje i napina sama — minimalna konserwacja",
    pt="Lubrifica e tensiona sozinha — manutenção mínima",
)
add(
    "🧰 Set di attrezzi e valigetta",
    cz="🧰 Sada nářadí a kufr",
    es="🧰 Juego de herramientas y maletín",
    hu="🧰 Szerszámkészlet és koffer",
    pl="🧰 Zestaw narzędzi i walizka",
    pt="🧰 Conjunto de ferramentas e mala",
)
add(
    "Tutto al suo posto, pronto da riporre",
    cz="Vše na svém místě, připraveno k uložení",
    es="Todo en su sitio, listo para guardar",
    hu="Minden a helyén, készen az elrakásra",
    pl="Wszystko na swoim miejscu, gotowe do schowania",
    pt="Tudo no sítio, pronto a arrumar",
)
add(
    "🛡️ Garanzia ufficiale 2 anni",
    cz="🛡️ Oficiální záruka 2 roky",
    es="🛡️ Garantía oficial de 2 años",
    hu="🛡️ Hivatalos 2 év garancia",
    pl="🛡️ Oficjalna gwarancja 2 lata",
    pt="🛡️ Garantia oficial de 2 anos",
)
add(
    "Assistenza inclusa — 30 giorni per il reso",
    cz="Servis v ceně — 30 dní na vrácení",
    es="Asistencia incluida: 30 días para la devolución",
    hu="Ügyfélszolgálat benne — 30 napos visszaküldés",
    pl="Wsparcie w zestawie — 30 dni na zwrot",
    pt="Assistência incluída — 30 dias para devolução",
)
add(
    "❓ Le domande più frequenti",
    cz="❓ Nejčastější otázky",
    es="❓ Las preguntas más frecuentes",
    hu="❓ A leggyakoribb kérdések",
    pl="❓ Najczęstsze pytania",
    pt="❓ As perguntas mais frequentes",
)
add(
    "Qualche dubbio? È normale.<br>",
    cz="Máte pochybnosti? To je v pořádku.<br>",
    es="¿Alguna duda? Es normal.<br>",
    hu="Van kérdése? Ez természetes.<br>",
    pl="Jakieś wątpliwości? To normalne.<br>",
    pt="Alguma dúvida? É normal.<br>",
)
add("Lo chiarisco tutto qui.", cz="Vše vysvětlím tady.", es="Lo aclaro todo aquí.", hu="Itt mindent tisztázok.", pl="Wszystko wyjaśniam tutaj.", pt="Esclareço tudo aqui.")
add(
    "Prima di ordinare, le risposte alle domande di sempre: consegna, pagamento, benzina, rami alti e reso.",
    cz="Než objednáte, odpovědi na obvyklé otázky: doručení, platba, benzín, vysoké větve a vrácení.",
    es="Antes de pedir, las respuestas de siempre: entrega, pago, gasolina, ramas altas y devolución.",
    hu="Rendelés előtt a szokásos kérdésekre a válasz: szállítás, fizetés, benzin, magas ágak és visszaküldés.",
    pl="Zanim zamówisz, odpowiedzi na stałe pytania: dostawa, płatność, benzyna, wysokie gałęzie i zwrot.",
    pt="Antes de encomendar, as respostas de sempre: entrega, pagamento, gasolina, ramos altos e devolução.",
)
add(
    "La consegna richiede circa 1–2 giorni lavorativi. ",
    cz="Doručení trvá přibližně 1–2 pracovní dny. ",
    es="La entrega tarda unos 1–2 días laborables. ",
    hu="A kézbesítés kb. 1–2 munkanap. ",
    pl="Dostawa trwa około 1–2 dni roboczych. ",
    pt="A entrega demora cerca de 1–2 dias úteis. ",
)
add(
    "Quando arriva l’ordine?",
    cz="Kdy objednávka dorazí?",
    es="¿Cuándo llega el pedido?",
    hu="Mikor érkezik a rendelés?",
    pl="Kiedy dotrze zamówienie?",
    pt="Quando chega a encomenda?",
)
add(
    "No. Paghi direttamente al corriere al momento della consegna. Niente carta. Niente anticipo.",
    cz="Ne. Platíte kurýrovi až při doručení. Žádná karta. Žádná záloha.",
    es="No. Pagas al repartidor en el momento de la entrega. Sin tarjeta. Sin adelanto.",
    hu="Nem. A futárnak fizet átvételkor. Nincs kártya. Nincs előleg.",
    pl="Nie. Płacisz kurierowi w momencie dostawy. Bez karty. Bez zaliczki.",
    pt="Não. Paga ao estafeta no momento da entrega. Sem cartão. Sem adiantamento.",
)
add(
    "Devo pagare in anticipo?",
    cz="Musím platit předem?",
    es="¿Tengo que pagar por adelantado?",
    hu="Előre kell fizetnem?",
    pl="Czy muszę płacić z góry?",
    pt="Tenho de pagar adiantado?",
)
add("Serve la benzina?", cz="Potřebuji benzín?", es="¿Hace falta gasolina?", hu="Kell benzin?", pl="Czy potrzebna jest benzyna?", pt="É precisa gasolina?")
add(
    "No. La Saw 7X™ funziona solo a batteria: due da 48 V e 8.000 mAh. Niente miscela, niente fumi, niente cavo di avviamento.",
    cz="Ne. Saw 7X™ je pouze na baterie: dvě 48 V a 8 000 mAh. Žádná směs, žádné zplodiny, žádná startovací šňůra.",
    es="No. La Saw 7X™ funciona solo a batería: dos de 48 V y 8.000 mAh. Sin mezcla, sin humos, sin cuerda de arranque.",
    hu="Nem. A Saw 7X™ csak akkumulátorral megy: kettő 48 V-os, 8000 mAh-s. Nincs keverék, nincs füst, nincs indítózsinór.",
    pl="Nie. Saw 7X™ działa tylko na akumulator: dwa 48 V i 8000 mAh. Bez mieszanki, bez spalin, bez linki rozrusznika.",
    pt="Não. A Saw 7X™ funciona só a bateria: duas de 48 V e 8.000 mAh. Sem mistura, sem fumos, sem corda de arranque.",
)
add(
    "Riesco a tagliare i rami alti senza scala?",
    cz="Zvládnu vysoké větve bez žebříku?",
    es="¿Puedo cortar las ramas altas sin escalera?",
    hu="Tudok magas ágakat vágni létra nélkül?",
    pl="Czy obetnę wysokie gałęzie bez drabiny?",
    pt="Consigo cortar os ramos altos sem escada?",
)
add(
    "Sì. L’asta telescopica arriva fino a 5 metri. Vicino al suolo usi il modo manuale compatto. In cima all’albero, monti l’asta.",
    cz="Ano. Teleskopická tyč dosáhne až 5 metrů. U země použijete kompaktní ruční režim. V koruně stromu nasadíte tyč.",
    es="Sí. La pértiga telescópica llega hasta 5 metros. Cerca del suelo usas el modo manual compacto. En la copa, montas la pértiga.",
    hu="Igen. A teleszkópos rúd akár 5 méterig elér. A talaj közelében a kompakt kézi módot használja. A fa tetején felteszi a rudat.",
    pl="Tak. Wysięgnik teleskopowy sięga do 5 metrów. Przy ziemi używasz trybu ręcznego. Na czubku drzewa montujesz wysięgnik.",
    pt="Sim. A haste telescópica chega até 5 metros. Perto do chão usa o modo manual compacto. No cimo da árvore, monta a haste.",
)
add(
    "E se poi non mi convince?",
    cz="A co když mě to nepřesvědčí?",
    es="¿Y si luego no me convence?",
    hu="És ha mégsem győz meg?",
    pl="A jeśli mnie nie przekona?",
    pt="E se depois não me convencer?",
)
add(
    "Hai 30 giorni per chiedere il reso, secondo le condizioni di rimborso. Non rischi niente.",
    cz="Máte 30 dní na vrácení podle podmínek reklamace. Nic neriskujete.",
    es="Tienes 30 días para pedir la devolución, según las condiciones de reembolso. No arriesgas nada.",
    hu="30 napja van a visszaküldésre a visszatérítési feltételek szerint. Semmit sem kockáztat.",
    pl="Masz 30 dni na zwrot zgodnie z warunkami refundacji. Niczego nie ryzykujesz.",
    pt="Tem 30 dias para pedir a devolução, segundo as condições de reembolso. Não arrisca nada.",
)
add(
    "✅ Paghi quando arriva",
    cz="✅ Platíte, až to dorazí",
    es="✅ Pagas cuando llega",
    hu="✅ Akkor fizet, amikor megérkezik",
    pl="✅ Płacisz, gdy dotrze",
    pt="✅ Paga quando chega",
)
add(
    "INSERISCI I DATI DI CONSEGNA",
    cz="ZADEJTE DORUČOVACÍ ÚDAJE",
    es="INTRODUCE LOS DATOS DE ENTREGA",
    hu="ADJA MEG A SZÁLLÍTÁSI ADATOKAT",
    pl="WPISZ DANE DOSTAWY",
    pt="INSIRA OS DADOS DE ENTREGA",
)
add(
    "L’ordine parte subito. Paghi solo alla consegna, direttamente al corriere.",
    cz="Objednávka jde hned. Platíte až při doručení, přímo kurýrovi.",
    es="El pedido sale enseguida. Pagas solo al recibir, directamente al repartidor.",
    hu="A rendelés azonnal elindul. Csak átvételkor fizet, közvetlenül a futárnak.",
    pl="Zamówienie rusza od razu. Płacisz tylko przy odbiorze, bezpośrednio kurierowi.",
    pt="A encomenda parte já. Paga só na entrega, diretamente ao estafeta.",
)
add(
    "Prodotti utili per la vita quotidiana, consegna in 24–48 ore con pagamento alla consegna.",
    cz="Užitečné produkty pro každodenní život, doručení do 24–48 hodin s platbou na dobírku.",
    es="Productos útiles para el día a día, entrega en 24–48 horas con pago contra reembolso.",
    hu="Hasznos termékek a mindennapi élethez, kézbesítés 24–48 óra alatt utánvétes fizetéssel.",
    pl="Przydatne produkty do codziennego życia, dostawa w 24–48 godzin z płatnością za pobraniem.",
    pt="Produtos úteis para o dia a dia, entrega em 24–48 horas com pagamento na entrega.",
)
add("Informazioni", cz="Informace", es="Información", hu="Információ", pl="Informacje", pt="Informação")
add("Chi siamo", cz="O nás", es="Sobre nosotros", hu="Rólunk", pl="O nas", pt="Sobre nós")
add("Contattaci", cz="Kontaktujte nás", es="Contáctenos", hu="Kapcsolat", pl="Kontakt", pt="Contate-nos")
add("Termini e Condizioni", cz="Obchodní podmínky", es="Términos y condiciones", hu="Általános szerződési feltételek", pl="Regulamin", pt="Termos e Condições")
add("Politica di Spedizione", cz="Doprava", es="Política de envío", hu="Szállítási feltételek", pl="Polityka dostawy", pt="Política de Envio")
add("Politica di Rimborso", cz="Vrácení zboží", es="Política de reembolso", hu="Visszaküldési szabályzat", pl="Polityka zwrotów", pt="Política de Reembolso")
add("Contatti", cz="Kontakt", es="Contacto", hu="Kapcsolat", pl="Kontakt", pt="Contato")
add("Tutti i diritti riservati.", cz="Všechna práva vyhrazena.", es="Todos los derechos reservados.", hu="Minden jog fenntartva.", pl="Wszelkie prawa zastrzeżone.", pt="Todos os direitos reservados.")
add("Invio...", cz="Odesílání...", es="Enviando...", hu="Küldés...", pl="Wysyłanie...", pt="A enviar...")
add(
    "Usiamo cookie tecnici e di terze parti per migliorare la tua esperienza e per analisi.",
    cz="Používáme technické soubory cookie a soubory cookie třetích stran ke zlepšení vašeho zážitku a k analýze.",
    es="Usamos cookies técnicas y de terceros para mejorar tu experiencia y para análisis.",
    hu="Technikai és harmadik féltől származó sütiket használunk az élmény javítása és elemzés céljából.",
    pl="Używamy technicznych plików cookie i plików cookie stron trzecich w celu poprawy doświadczenia i analizy.",
    pt="Usamos cookies técnicos e de terceiros para melhorar a sua experiência e para análises.",
)
add("Accetta", cz="Přijmout", es="Aceptar", hu="Elfogadom", pl="Akceptuję", pt="Aceitar")
add("Scopri di più", cz="Zjistit více", es="Más información", hu="Tudj meg többet", pl="Dowiedz się więcej", pt="Saber mais")

# Titles / meta / schema / alts that include product type
add(
    "Saw 7X™ — Motosega elettrica telescopica | ",
    cz="Saw 7X™ — Elektrická teleskopická pila | ",
    es="Saw 7X™ — Motosierra eléctrica telescópica | ",
    hu="Saw 7X™ — Teleszkópos elektromos láncfűrész | ",
    pl="Saw 7X™ — Elektryczna pilarka teleskopowa | ",
    pt="Saw 7X™ — Motosserra elétrica telescópica | ",
)
add(
    "Saw 7X™: taglia i rami a 5 metri e il legno fino a 35 cm, senza scala e senza benzina. 2 batterie 48 V. Pagamento alla consegna. Oggi ",
    cz="Saw 7X™: řeže větve v 5 metrech a dřevo až do 35 cm, bez žebříku a bez benzínu. 2 baterie 48 V. Platba na dobírku. Dnes ",
    es="Saw 7X™: corta ramas a 5 metros y madera de hasta 35 cm, sin escalera y sin gasolina. 2 baterías 48 V. Pago contra reembolso. Hoy ",
    hu="Saw 7X™: 5 méteren vágja az ágakat és akár 35 cm-es fát, létra és benzin nélkül. 2 darab 48 V-os akku. Utánvét. Ma ",
    pl="Saw 7X™: przycina gałęzie na 5 metrach i drewno do 35 cm, bez drabiny i bez benzyny. 2 akumulatory 48 V. Płatność przy odbiorze. Dziś ",
    pt="Saw 7X™: corta ramos a 5 metros e madeira até 35 cm, sem escada e sem gasolina. 2 baterias 48 V. Pagamento na entrega. Hoje ",
)
add(
    " invece di ",
    cz=" místo ",
    es=" en lugar de ",
    hu=" helyett ",
    pl=" zamiast ",
    pt=" em vez de ",
)
add(
    "Motosega elettrica telescopica. Taglia il legno fino a 35 cm di diametro, arriva a 5 metri e pesa 700 g. SuperChain X™ lubrifica e tende la catena da sola. 2 batterie 48 V.",
    cz="Elektrická teleskopická pila. Řeže dřevo o průměru až 35 cm, dosáhne 5 metrů a váží 700 g. SuperChain X™ maže a napíná řetěz sama. 2 baterie 48 V.",
    es="Motosierra eléctrica telescópica. Corta madera de hasta 35 cm de diámetro, llega a 5 metros y pesa 700 g. SuperChain X™ lubrica y tensa la cadena sola. 2 baterías 48 V.",
    hu="Teleszkópos elektromos láncfűrész. Akár 35 cm átmérőjű fát vág, 5 méterig elér, 700 g. A SuperChain X™ magától keni és feszíti a láncot. 2 darab 48 V-os akku.",
    pl="Elektryczna pilarka teleskopowa. Tnie drewno o średnicy do 35 cm, sięga 5 metrów i waży 700 g. SuperChain X™ smaruje i napina łańcuch sama. 2 akumulatory 48 V.",
    pt="Motosserra elétrica telescópica. Corta madeira até 35 cm de diâmetro, chega a 5 metros e pesa 700 g. SuperChain X™ lubrifica e tensiona a corrente sozinha. 2 baterias 48 V.",
)
add("Kit completo Saw 7X™", cz="Kompletní sada Saw 7X™", es="Kit completo Saw 7X™", hu="Teljes Saw 7X™ készlet", pl="Kompletny zestaw Saw 7X™", pt="Kit completo Saw 7X™")

# Thank-you
add(
    "Ordine ricevuto — Attendi la chiamata di conferma | Saw 7X™",
    cz="Objednávka přijata — Čekejte na potvrzovací hovor | Saw 7X™",
    es="Pedido recibido — Espere la llamada de confirmación | Saw 7X™",
    hu="Rendelés rögzítve — Várja a megerősítő hívást | Saw 7X™",
    pl="Zamówienie przyjęte — Czekaj na telefon potwierdzający | Saw 7X™",
    pt="Encomenda recebida — Aguarde a chamada de confirmação | Saw 7X™",
)
add(
    "Il tuo ordine Saw 7X™ è stato registrato. Manca solo un ultimo passaggio: rispondi alla chiamata di conferma del nostro operatore.",
    cz="Vaše objednávka Saw 7X™ byla zaregistrována. Zbývá poslední krok: odpovězte na potvrzovací hovor našeho operátora.",
    es="Tu pedido Saw 7X™ ha sido registrado. Solo falta un último paso: responde a la llamada de confirmación de nuestro operador.",
    hu="Saw 7X™ rendelését rögzítettük. Már csak egy utolsó lépés van: vegye fel operátorunk megerősítő hívását.",
    pl="Twoje zamówienie Saw 7X™ zostało zarejestrowane. Został ostatni krok: odbierz telefon potwierdzający od naszego operatora.",
    pt="A sua encomenda Saw 7X™ foi registada. Falta só um último passo: atenda a chamada de confirmação do nosso operador.",
)
add(
    "Il tuo ordine Saw 7X™ è stato registrato!",
    cz="Vaše objednávka Saw 7X™ byla zaregistrována!",
    es="¡Tu pedido Saw 7X™ ha sido registrado!",
    hu="Saw 7X™ rendelését rögzítettük!",
    pl="Twoje zamówienie Saw 7X™ zostało zarejestrowane!",
    pt="A sua encomenda Saw 7X™ foi registada!",
)
add(
    "Perfetto — il tuo ordine è in elaborazione. Manca solo <strong>un ultimo passaggio</strong> per completarlo e far partire la spedizione.",
    cz="Skvělé — objednávka se zpracovává. Zbývá jen <strong>poslední krok</strong> k dokončení a odeslání.",
    es="Perfecto: tu pedido se está procesando. Solo falta <strong>un último paso</strong> para completarlo y enviar el paquete.",
    hu="Remek — a rendelés feldolgozás alatt van. Már csak <strong>egy utolsó lépés</strong> kell a befejezéshez és a feladáshoz.",
    pl="Świetnie — zamówienie jest przetwarzane. Został tylko <strong>ostatni krok</strong>, by je dokończyć i nadać przesyłkę.",
    pt="Perfeito — a encomenda está a ser processada. Falta só <strong>um último passo</strong> para a concluir e enviar.",
)
add(
    "Saw 7X™ — motosega elettrica telescopica",
    cz="Saw 7X™ — elektrická teleskopická pila",
    es="Saw 7X™ — motosierra eléctrica telescópica",
    hu="Saw 7X™ — teleszkópos elektromos láncfűrész",
    pl="Saw 7X™ — elektryczna pilarka teleskopowa",
    pt="Saw 7X™ — motosserra elétrica telescópica",
)
add(
    "Kit completo · Pagamento alla consegna",
    cz="Kompletní sada · Platba na dobírku",
    es="Kit completo · Pago contra reembolso",
    hu="Teljes készlet · Utánvétes fizetés",
    pl="Kompletny zestaw · Płatność przy odbiorze",
    pt="Kit completo · Pagamento na entrega",
)
add(
    "Il team devicefindhub al lavoro: call center e logistica COD",
    cz="Tým devicefindhub v práci: call centrum a logistika dobírky",
    es="El equipo devicefindhub en marcha: call center y logística contra reembolso",
    hu="A devicefindhub csapat munka közben: call center és utánvétes logisztika",
    pl="Zespół devicefindhub w pracy: call center i logistyka pobrania",
    pt="A equipa devicefindhub ao trabalho: call center e logística contra reembolso",
)
add("👇 Cosa devi fare adesso", cz="👇 Co teď udělat", es="👇 Qué debes hacer ahora", hu="👇 Mit tegyen most", pl="👇 Co zrobić teraz", pt="👇 O que deve fazer agora")
add(
    "📞 Rispondi alla chiamata di conferma",
    cz="📞 Odpovězte na potvrzovací hovor",
    es="📞 Responde a la llamada de confirmación",
    hu="📞 Vegye fel a megerősítő hívást",
    pl="📞 Odbierz telefon potwierdzający",
    pt="📞 Atenda a chamada de confirmação",
)
add(
    "Un nostro operatore ti contatterà <strong>nelle prossime ore</strong> per confermare il tuo ordine Saw 7X™.",
    cz="Náš operátor vás bude kontaktovat <strong>v nejbližších hodinách</strong> kvůli potvrzení objednávky Saw 7X™.",
    es="Un operador te contactará <strong>en las próximas horas</strong> para confirmar tu pedido Saw 7X™.",
    hu="Operátorunk <strong>a következő órákban</strong> felhívja a Saw 7X™ rendelés megerősítéséhez.",
    pl="Nasz operator skontaktuje się z Tobą <strong>w najbliższych godzinach</strong>, aby potwierdzić zamówienie Saw 7X™.",
    pt="Um operador vai contactá-lo <strong>nas próximas horas</strong> para confirmar a encomenda Saw 7X™.",
)
add(
    "Se non rispondi alla chiamata, l'ordine verrà automaticamente annullato.",
    cz="Pokud na hovor neodpovíte, objednávka bude automaticky zrušena.",
    es="Si no respondes a la llamada, el pedido se cancelará automáticamente.",
    hu="Ha nem veszi fel a hívást, a rendelés automatikusan törlődik.",
    pl="Jeśli nie odbierzesz telefonu, zamówienie zostanie automatycznie anulowane.",
    pt="Se não atender a chamada, a encomenda será cancelada automaticamente.",
)
add("🕒 Orari di contatto", cz="🕒 Hodiny kontaktu", es="🕒 Horario de contacto", hu="🕒 Elérhetőségi idő", pl="🕒 Godziny kontaktu", pt="🕒 Horário de contacto")
add(
    "Lunedì – Sabato · 9:00 – 18:00",
    cz="Pondělí – sobota · 9:00 – 18:00",
    es="Lunes – sábado · 9:00 – 18:00",
    hu="Hétfő – szombat · 9:00 – 18:00",
    pl="Poniedziałek – sobota · 9:00 – 18:00",
    pt="Segunda – sábado · 9:00 – 18:00",
)
add("📋 Cosa succede dopo", cz="📋 Co bude dál", es="📋 Qué pasa después", hu="📋 Mi történik ezután", pl="📋 Co dalej", pt="📋 O que acontece a seguir")
add(
    "Rispondi alla chiamata e <strong>conferma i tuoi dati</strong>",
    cz="Odpovězte na hovor a <strong>potvrďte své údaje</strong>",
    es="Responde a la llamada y <strong>confirma tus datos</strong>",
    hu="Vegye fel a hívást és <strong>erősítse meg az adatait</strong>",
    pl="Odbierz telefon i <strong>potwierdź swoje dane</strong>",
    pt="Atenda a chamada e <strong>confirme os seus dados</strong>",
)
add(
    "La tua Saw 7X™ verrà spedita entro <strong>24–48 ore</strong>",
    cz="Vaše Saw 7X™ odejde do <strong>24–48 hodin</strong>",
    es="Tu Saw 7X™ se enviará en <strong>24–48 horas</strong>",
    hu="Saw 7X™ készletét <strong>24–48 órán belül</strong> feladjuk",
    pl="Twoja Saw 7X™ zostanie wysłana w ciągu <strong>24–48 godzin</strong>",
    pt="A sua Saw 7X™ será enviada em <strong>24–48 horas</strong>",
)
add(
    "Consegna a domicilio e <strong>pagamento alla consegna</strong>",
    cz="Doručení až domů a <strong>platba na dobírku</strong>",
    es="Entrega a domicilio y <strong>pago contra reembolso</strong>",
    hu="Házhozszállítás és <strong>utánvétes fizetés</strong>",
    pl="Dostawa pod drzwi i <strong>płatność przy odbiorze</strong>",
    pt="Entrega ao domicílio e <strong>pagamento na entrega</strong>",
)
add("🔒 Pagamento alla consegna", cz="🔒 Platba na dobírku", es="🔒 Pago contra reembolso", hu="🔒 Utánvétes fizetés", pl="🔒 Płatność przy odbiorze", pt="🔒 Pagamento na entrega")
add("🛡️ Garanzia 2 anni", cz="🛡️ Záruka 2 roky", es="🛡️ Garantía de 2 años", hu="🛡️ 2 év garancia", pl="🛡️ Gwarancja 2 lata", pt="🛡️ Garantia de 2 anos")
add("Tutti i diritti riservati.", cz="Všechna práva vyhrazena.", es="Todos los derechos reservados.", hu="Minden jog fenntartva.", pl="Wszelkie prawa zastrzeżone.", pt="Todos os direitos reservados.")

FOOTER_POLICY = {
    "cz": ("Zásady ochrany osobních údajů", "Zásady cookies"),
    "es": ("política de privacidad", "Política de cookies"),
    "hu": ("Adatvédelmi szabályzat", "Cookie szabályzat"),
    "pl": ("Polityka prywatności", "Polityka cookies"),
    "pt": ("política de Privacidade", "Política de Cookies"),
}

PLACEHOLDERS = {
    "cz": ("Jan Novák", "+420 777 123 456", "Václavské nám. 1, 110 00 Praha"),
    "es": ("María García", "+34 612 345 678", "Calle Mayor 1, 28013 Madrid"),
    "hu": ("Kovács János", "+36 30 123 4567", "Andrássy út 1, 1061 Budapest"),
    "it": ("Mario Rossi", "+39 392 0745623", "Via Torino 1, 12345 Roma Italia"),
    "pl": ("Jan Kowalski", "+48 600 123 456", "ul. Marszałkowska 1, 00-001 Warszawa"),
    "pt": ("João Silva", "+351 912 345 678", "Rua Augusta 1, 1100-048 Lisboa"),
}


def apply_copy(html: str, geo: str) -> str:
    if geo != "it":
        pairs = sorted(T[geo].items(), key=lambda kv: len(kv[0]), reverse=True)
        for src, dst in pairs:
            html = html.replace(src, dst)
        priv, cookie = FOOTER_POLICY[geo]
        html = html.replace(">Privacy Policy<", f">{priv}<")
        html = html.replace(">Cookie Policy<", f">{cookie}<")
    name, tel, addr = PLACEHOLDERS[geo]
    html = html.replace('placeholder="Mario Rossi"', f'placeholder="{name}"')
    html = html.replace('placeholder="+39 392 0745623"', f'placeholder="{tel}"')
    html = html.replace('placeholder="Via Torino 1, 12345 Roma Italia"', f'placeholder="{addr}"')
    return html


def apply_geo(html: str, geo: str, cfg: dict) -> str:
    html = html.replace('lang="it"', f'lang="{cfg["lang"]}"')
    html = html.replace("/it/saw7x/", f"/{geo}/saw7x/")
    html = html.replace("https://devicefindhub.com/it/", f"https://devicefindhub.com/{geo}/")
    html = html.replace('href="/it/', f'href="/{geo}/')
    html = html.replace("GEO: 'it'", f"GEO: '{geo}'")
    html = html.replace("OFFER_NAME: 'Saw 7X™ IT'", f"OFFER_NAME: 'Saw 7X™ {geo.upper()}'")
    html = html.replace("LP_ID: 'it-saw7x'", f"LP_ID: '{geo}-saw7x'")
    html = html.replace("CURRENCY: 'EUR'", f"CURRENCY: '{cfg['currency']}'")
    html = html.replace("PRICE: 79.99", f"PRICE: {cfg['price']}")
    html = html.replace('"price": "79.99"', f'"price": "{cfg["schema_price"]}"')
    html = html.replace('"priceCurrency": "EUR"', f'"priceCurrency": "{cfg["currency"]}"')
    html = html.replace("79,99€", cfg["price_display"])
    html = html.replace("159,98€", cfg["old_price_display"])
    html = html.replace("a soli 79,99€", f"a soli {cfg['price_display']}")
    html = html.replace("Consegna in tutta Italia, in 24–48 ore.", f"Consegna {cfg['country_prep']}, in 24–48 ore.")
    html = html.replace("Spedizione gratuita in tutta Italia.", f"Spedizione gratuita {cfg['country_prep']}.")
    return html


def translate_country_sentences(html: str, geo: str, cfg: dict) -> str:
    if geo == "it":
        return html
    replacements = {
        "cz": (
            ("a soli ", "za pouhých "),
            ("Consegna po celé ČR, in 24–48 ore.", "Doručení po celé ČR do 24–48 hodin."),
            ("Spedizione gratuita po celé ČR.", "Doprava zdarma po celé ČR."),
        ),
        "es": (
            ("a soli ", "por solo "),
            ("Consegna en toda España, in 24–48 ore.", "Entrega en toda España, en 24–48 horas."),
            ("Spedizione gratuita en toda España.", "Envío gratis en toda España."),
        ),
        "hu": (
            ("a soli ", "csak "),
            ("Consegna egész Magyarországon, in 24–48 ore.", "Kézbesítés egész Magyarországon 24–48 óra alatt."),
            ("Spedizione gratuita egész Magyarországon.", "Ingyenes szállítás egész Magyarországon."),
        ),
        "pl": (
            ("a soli ", "za jedyne "),
            ("Consegna w całej Polsce, in 24–48 ore.", "Dostawa w całej Polsce w 24–48 godzin."),
            ("Spedizione gratuita w całej Polsce.", "Darmowa dostawa w całej Polsce."),
        ),
        "pt": (
            ("a soli ", "por apenas "),
            ("Consegna em todo o Portugal, in 24–48 ore.", "Entrega em todo o Portugal, em 24–48 horas."),
            ("Spedizione gratuita em todo o Portugal.", "Envio grátis em todo o Portugal."),
        ),
    }
    for old, new in replacements[geo]:
        html = html.replace(old, new)
    return html


def write_index(geo: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="{GEOS[geo]['lang']}">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-18437776204"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());

  gtag('config', 'AW-18437776204');
  gtag('config', 'AW-18376580748');
</script>
<meta charset="utf-8">
<title>Redirect…</title>
<script>
(function () {{
  var path = '/{geo}/saw7x/landing.html';
  window.location.replace(path + window.location.search + window.location.hash);
}})();
</script>
<meta http-equiv="refresh" content="0;url=/{geo}/saw7x/landing.html">
<link rel="canonical" href="https://devicefindhub.com/{geo}/saw7x/landing.html">
</head>
<body>
<p><a href="/{geo}/saw7x/landing.html">Saw 7X™</a></p>
</body>
</html>
"""


def update_sitemap(geos: list[str]) -> None:
    path = ROOT / "sitemap.xml"
    xml = path.read_text(encoding="utf-8")
    block = []
    for geo in geos:
        for loc in (f"https://devicefindhub.com/{geo}/saw7x/", f"https://devicefindhub.com/{geo}/saw7x/landing.html"):
            entry = f"  <url><loc>{loc}</loc><lastmod>2026-09-09</lastmod><changefreq>weekly</changefreq><priority>0.95</priority></url>\n"
            if loc not in xml:
                block.append(entry)
    if not block:
        return
    xml = xml.replace(
        "  <url><loc>https://devicefindhub.com/it/saw7x/landing.html</loc><lastmod>2026-09-09</lastmod><changefreq>weekly</changefreq><priority>0.95</priority></url>\n",
        "  <url><loc>https://devicefindhub.com/it/saw7x/landing.html</loc><lastmod>2026-09-09</lastmod><changefreq>weekly</changefreq><priority>0.95</priority></url>\n"
        + "".join(block),
        1,
    )
    path.write_text(xml, encoding="utf-8")


def main() -> None:
    src_landing = (ROOT / "it/saw7x/landing.html").read_text(encoding="utf-8")
    src_ty = (ROOT / "it/saw7x/thank-you.html").read_text(encoding="utf-8")

    for geo, cfg in GEOS.items():
        dest = ROOT / geo / "saw7x"
        dest.mkdir(parents=True, exist_ok=True)
        landing = apply_geo(src_landing, geo, cfg)
        landing = apply_copy(landing, geo)
        landing = translate_country_sentences(landing, geo, cfg)
        ty = apply_geo(src_ty, geo, cfg)
        ty = apply_copy(ty, geo)
        (dest / "landing.html").write_text(landing, encoding="utf-8")
        (dest / "thank-you.html").write_text(ty, encoding="utf-8")
        (dest / "index.html").write_text(write_index(geo), encoding="utf-8")
        print(f"wrote {geo}/saw7x/")

    update_sitemap(list(GEOS))
    print("sitemap updated")


if __name__ == "__main__":
    main()
