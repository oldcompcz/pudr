# -*- coding: utf-8 -*-

texts = {
    'command_names': [
        'Zkoumej',
        'Jdi',
        'Vezmi',
        'Použij',
        'Otevři',
        'Konec',
    ],

    'texts_intro': [
        # 0
        '(c) 7t7 Studios_(c) myrmica habilis__github.com/oldcompcz/pudr',
        # 1
        'pro soutěž__"Tvorba hry pro DOS"__#hvdosdev2019_www.high-voltage.cz',
        # 2
        'verze 1.0__30.8.2019',
        # 3
        'Probudila tě nesnesitelná zima a iritující zvuk kapek pravidelně'
        ' dopadajících na lesklé dlaždice.',
        # 4
        'Ležíš v márnici ve zpola vysunutém chladicím šuplíku na mrtvoly.',
        # 5
        'Trápí tě bolest hlavy a neblahý pocit, že neschází mnoho, aby ses stal'
        ' jednou ze zde uskladněných položek.',
    ],

    'room_descriptions': [
        # 0
        'Jsi v chladném sále márnice. Ve slabém svitu jediné žárovky vidíš řadu'
        ' šuplíků na mrtvoly.',
        # 1
        'Jsi na pitevně. Vidíš bílé dveře s červeným nápisem "LABORATOŘ -'
        ' nepovolaným vstup zakázán".',
        # 2
        'Jsi na záchodě.',
        # 3
        'Vešel jsi do zšeřelé laboratoře se zažloutlými stěnami bez oken.',
        # 4
        'Jsi v ředitelově pracovně. Nad psacím stolem je malé zamřížované'
        ' okénko.',
        # 5
        'Jsi v krematoriu.',
        # 6
        'Jsi v přípravně a úpravně zemřelých.',
        # 7
        'Vstoupil jsi do prostorného skladiště vykazujícího akutní potřebu'
        ' totální debordelizace.',
        # 8
        'Vlezl jsi do nitra kremační pece. Je tu příjemně teplo.',
        # 9
        'Stojíš v reprezentativní prostorné hale pohřebního ústavu. Je'
        ' vymalována veselými barvami.',
        # 10
        'Stojíš na konci dlouhé chodby u zamčených ocelových dveří vedoucích'
        ' někam ven.',
        # 11
        'Jsi na chodbě. Jsou tu otlučené dveře označené cedulkou WC.',
        # 12
        'Jdeš po chodbě. Podlaha je do čista vytřená špinavou vodou.',
        # 13
        'Jsi na chodbě. Jsou tu oprýskané dveře označené tabulkou PITEVNA.',
        # 14
        'Jsi na chodbě. Jsou tu masivní dvojité dveře označené tabulkou'
        ' MÁRNICE.',
        # 15
        'Jdeš po chodbě. Nad hlavou máš blikající zářivku a pod nohama ošlapané'
        ' PVC zelenavé barvy.',
        # 16
        'Jsi na chodbě. Jsou tu zamřížované dveře označené obřím nápisem'
        ' SKLAD.',
        # 17
        'Jsi na chodbě. Jsou tu polstrované dveře označené tabulkou PŘÍPRAVNA.',
        # 18
        'Stojíš na začátku chodby. Za zamčenými prosklenými dveřmi vidíš'
        ' osvětlenou halu.',
        # 19
        'Vešel jsi do jakéhosi salónku či malého obývacího pokoje.',
        # 20
        'Nacházíš se v nevlídně působící recepci této obskurní instituce.',
        # 21
        'Vlezl jsi do kuchyňky. Všude se válí láhve a plechovky pivních značek'
        ' Zubr a Kozel.',
        # 22
        'Jsi v malé chodbičce s ošoupaným kobercem.',
        # 23
        'Vylezl jsi na dvorek obehnaný vysokou zdí. Venku je ještě tma.',
        # 24
        'Jsi na ulici před pohřebním_ústavem. Podařilo se ti_uprchnout a tím'
        ' jsi dovedl_do konce tuto hříčku.__Blahopřeji.',
    ],

    'room_exits': [
        # 10: 11; 12< 13= 14> 15? 16@ 17A 18B 19C 20D 21E 22F 23G 24H
        # 0
        [14],
        # 1
        [13, 3],
        # 2
        [11],
        # 3
        [1],
        # 4
        [9, 22],
        # 5
        [6, 8],
        # 6
        [17, 5],
        # 7
        [16],
        # 8
        [5],
        # 9
        [18, 4, 20],
        # 10
        [11],
        # 11
        [10, 2, 12],
        # 12
        [13],
        # 13
        [12, 1, 14],
        # 14
        [13, 0, 15],
        # 15
        [14, 16],
        # 16
        [15, 7, 17],
        # 17
        [16, 6, 18],
        # 18
        [17],
        # 19
        [22],
        # 20
        [9],
        # 21
        [22],
        # 22
        [4, 19, 21],
        # 23
        [10],
        # 24
        [20],
    ],

    'exit_names': [
        # 0
        'do márnice',
        # 1
        'na pitevnu',
        # 2
        'na WC',
        # 3
        'do laboratoře',
        # 4
        'do kanceláře',
        # 5
        'do krematoria',
        # 6
        'do přípravny',
        # 7
        'do skladu',
        # 8
        'do pece',
        # 9
        'do haly',
        # 10
        'na chodbu',
        # 11
        'na chodbu',
        # 12
        'na chodbu',
        # 13
        'na chodbu',
        # 14
        'na chodbu',
        # 15
        'na chodbu',
        # 16
        'na chodbu',
        # 17
        'na chodbu',
        # 18
        'na chodbu',
        # 19
        'do pokoje',
        # 20
        'na recepci',
        # 21
        'do kuchyňky',
        # 22
        'na chodbičku',
        # 23
        'ven',
        # 24
        'ven',
    ],

    'texts_short': [
        # 0
        'Budiž.',
        # 1
        'Nevím jak.',
        # 2
        'Sundal sis brýle.',
        # 3
        'Nasadil sis brýle.',
        # 4
        'Jedno bude stačit.',
        # 5
        'Odemkl jsi dveře do haly.',
        # 6
        'Odemkl jsi zadní vchod budovy.',
        # 7
        'Je zamčená.',
        # 8
        'Odejít do DOSu',
        # 9
        'Zdá se, že je po_smrti.',
    ],

    'texts_middle': [
        # 0
        'Je pevně zavřená a zatlučená několika hřebíky.',
        # 1
        'Vypáčil a vytahal jsi hřeby z víka rakve.',
        # 2
        'Odhrnul jsi vrstvu popela a odkryl nějaké zapomenuté lidské'
        ' pozůstatky.',
        # 3
        'Použil jsi femur coby páčidlo a vylomil dvířka skříňky.',
        # 4
        'Objevil jsi lahvinku, která by se mohla hodit.',
    ],

    'texts_other': [
        # 0
        'Provedl jsi vertikální řez přední částí trupu nebohého zesnulého.',
        # 1
        'Rozevřel jsi čerstvou ránu na mrtvém těle. Je plná nevábně zapáchající'
        ' tekutiny.',
        # 2
        'Role měkkého papíru nacucala odpornou kapalinu z rány a s plesknutím'
        ' dopadla na podlahu.',
        # 3
        'Při bližším pohledu vidíš, že chlap má zlomené žebro, neodborně'
        ' vyspravené kusem drátu.',
        # 4
        'Propojil jsi pahýly vodičů a lucerna se neochotně rozsvítila. Proti'
        ' světlu se zaleskla pavučina.',
        # 5
        'Ze škvíry ve zdivu vyběhl velký pavouk, aby obhlédl, co se to děje.',
        # 6
        'Namaloval sis úděsné kruhy pod očima. Vypadáš jako opravdová oživlá'
        ' mrtvola.',
        # 7
        'Hodil jsi popuzeného arachnida na masitý zátylek recepční. Ta s'
        ' hlasitým jekotem opustila budovu.',
        # 8
        'Odklopil jsi víko rakve a nakoukl dovnitř. Je prázdná, uvnitř leží jen'
        ' něčí falešné zuby.',
        # 9
        'Dědek zajásal, že má zase zuby, a věnoval ti svůj dosavadní nástroj na'
        ' porcování potravy.',
        # 10
        'Po spatření chodící mrtvoly s plandajícím okem, která přilezla odněkud'
        ' z márnice, bába odfuněla do dáli.',
        # 11
        'Nalil jsi trochu vrchnímu funebrákovi do úst. Pravá ruka mu po chvíli'
        ' bezvládně vypadla z kapsy saka.',
        # 12
        'S krajním sebezapřením jsi provedl improvizovanou amputaci ještě teplé'
        ' končetiny.',
        # 13
        'Patentní klíč do dozického_zámku nezasuneš._A zasuneš-li, neotočíš._A'
        ' otočíš-li, neodemkneš.',
        # 14
        'Ač postrádáš patřičnou manuální zručnost, nebožtíka jsi zase jakž takž'
        ' zašil.',
        # 15
        'Nastražil jsi pavučinu na zeď ke stropu. Bába spatřila nevysmýčený'
        ' kout a odvalila se hledat smeták.',
        # 16
        'Už je tady zas a svou tělesnou stavbou opět brání v průchodu chodbou.',
    ]

}


things = [

    {  # 0
        'name': 'lucernu',
        'where': 23,
        'portable': False,
        'image': 'LUCERNA',
        'slot': 2,
        'description': 'Stylové venkovní svítidlo. Někdo ze zdi vyrval jeden'
                       ' drát, lampa tudíž nesvítí.',
    },

    {  # 1
        'name': 'rakev',
        'where': 5,
        'portable': False,
        'image': 'RAKEV',
        'slot': 0,
        'description': 'Futrál na poslední cestu.',
    },

    {  # 2
        'name': 'mrtvolu',
        'where': 0,
        'portable': False,
        'image': 'MRTVOLA',
        'slot': 0,
        'description': 'Ošklivě potlučené tělo muže ležící na studené nerezové'
                       ' desce stolu.',
    },

    {  # 3
        'name': 'skladníka',
        'where': 7,
        'portable': False,
        'image': 'SKLADNIK',
        'slot': 2,
        'description': 'Starý páprda s veselýma očima a bezzubým úsměvem.',
    },

    {  # 4
        'name': 'oči',
        'where': 3,
        'portable': True,
        'image': 'OCI',
        'slot': 2,
        'description': 'Zavařovací sklenice plná lidských zrakových orgánů.'
                       ' Některé po tobě pokukují.',
    },

    {  # 5
        'name': 'jehlu a nit',
        'where': 1,
        'portable': True,
        'image': 'JEHLA',
        'slot': 2,
        'description': 'Souprava na zašívání čerstvých absolventů pitvy.',
    },

    {  # 6
        'name': 'líčidla',
        'where': 6,
        'portable': True,
        'image': 'LICIDLA',
        'slot': 0,
        'description': 'Malůvky pro zkrášlení těch, kterým už je všechno'
                       ' jedno.',
    },

    {  # 7
        'name': 'brýle',
        'where': 4,
        'portable': True,
        'image': 'BRYLE',
        'slot': 0,
        'description': 'Luxusní brýle značky BluRayBan, potlačující modrou'
                       ' složku světla.',
    },

    {  # 8
        'name': 'pilu',
        'where': 6,
        'portable': True,
        'image': 'PILA',
        'slot': 2,
        'description': 'Některé nepřizpůsobivé umrlce je třeba do rakve trochu'
                       ' přikrátit.',
    },

    {  # 9
        'name': 'doc. Rakwowitze',
        'where': 19,
        'portable': False,
        'image': 'REDITEL',
        'slot': 1,
        'description': 'V čalouněné sesli leží sám Doc. MUDr. Horst Rakwowitz,'
                       ' CSc. a chrápe s otevřenou pusou.',
    },

    {  # 10
        'name': 'hajzlpapír',
        'where': 2,
        'portable': True,
        'image': 'HAJZLPAPIR',
        'slot': 1,
        'description': '"Na záchode nie si sám, je tam s tebou Harmasan."',
    },

    {  # 11
        'name': 'pavouka',
        'where': 49,
        'portable': True,
        'image': 'PAVOUK',
        'slot': 0,
        'description': 'Statný exemplář křižáka obecného.',
    },

    {  # 12
        'name': 'zubní protézu',
        'where': 49,
        'portable': True,
        'image': 'ZUBY',
        'slot': 2,
        'description': 'Nepříliš zdařilá, ale přesto usměvavá náhrada lidského'
                       ' chrupu.',
    },

    {  # 13
        'name': 'drát',
        'where': 49,
        'portable': True,
        'image': 'DRAT',
        'slot': 2,
        'description': 'Kus měděného drátu obalený svinstvem.',
    },

    {  # 14
        'name': 'pavučinu',
        'where': 49,
        'portable': True,
        'image': 'PAVUCINA',
        'slot': 0,
        'description': 'Převelice jemné předivo.',
    },

    {  # 15
        'name': 'žiletku',
        'where': 49,
        'portable': True,
        'image': 'ZILETKA',
        'slot': 0,
        'description': 'Stále ostrá čepelka Astra.',
    },

    {  # 16
        'name': 'recepční',
        'where': 20,
        'portable': False,
        'image': 'RECEPCNI',
        'slot': 0,
        'description': 'Kolem plnoštíhlé dozorčí stěží projdeš ven, aniž bys'
                       ' vyvolal poplach.',
    },

    {  # 17
        'name': 'otvírák',
        'where': 21,
        'portable': True,
        'image': 'OTVIRAK',
        'slot': 2,
        'description': 'Multi(2)funkční otvírák na konzervy a pivní zátky.',
    },

    {  # 18
        'name': 'uklízečku',
        'where': 12,
        'portable': False,
        'image': 'UKLIZECKA',
        'slot': 1,
        'description': 'Kulatá bába v zástěře je o dvě hlavy menší, zato svou'
                       ' postavou zabírá celou šířku chodby.',
    },

    {  # 19
        'name': 'jed',
        'where': 49,
        'portable': True,
        'image': 'JED',
        'slot': 1,
        'description': 'Jakýsi utrejch neznámého původu uzavřený v baňaté'
                       ' láhvi.',
    },

    {  # 20
        'name': 'oko',
        'where': 49,
        'portable': True,
        'image': 'OKO',
        'slot': 1,
        'description': 'Slepá bulva upírá svůj kalný pohled k zemi.',
    },

    {  # 21
        'name': 'ruku',
        'where': 49,
        'portable': False,
        'image': 'RUKAKLIC',
        'slot': 0,
        'description': 'Ruka třímá nějaký klíček, leč bohužel tak křečovitě, že'
                       ' ho nelze vyprostit.',
    },

    {  # 22
        'name': 'stehna',
        'where': 21,
        'portable': True,
        'image': 'STEHNA',
        'slot': 0,
        'description': 'Párek sexy žabích stehýnek na plastovém talířku.',
    },

    {  # 23
        'name': 'klíč',
        'where': 49,
        'portable': True,
        'image': 'KLIC',
        'slot': 2,
        'description': 'Klíč, jenž při úprku vypadl uklízečce z kapsy.',
    },

    {  # 24
        'name': 'kost',
        'where': 49,
        'portable': True,
        'image': 'FEMUR',
        'slot': 0,
        'description': 'Zachovalá stehenní kost dospělého člověka.',
    },

    {  # 25
        'name': 'skříň',
        'where': 3,
        'portable': False,
        'image': 'SKRIN',
        'slot': 0,
        'description': 'Plechová vitrínová skříň s léčivy a jinými'
                       ' chemikáliemi.',
    },

    {  # 26
        'name': 'smeták',
        'where': 49,
        'portable': True,
        'image': 'SMETAK',
        'slot': 0,
        'description': 'Standardní ruční čistič podlah bez přídavných funkcí.',
    },

    {  # 27
        'name': 'zub',
        'where': 49,
        'portable': True,
        'image': 'ZUB',
        'slot': 2,
        'description': 'Stolička zkažená až běda.',
    },
]
