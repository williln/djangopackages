import datetime

from datetime import timedelta
from django.contrib.auth.models import User
from django.utils.timezone import make_aware, now

from package.models import Category, Package, Version, Commit
from profiles.models import Profile


abandoned_package_last_commit = make_aware(
    datetime.datetime(now().year - 2, now().month, now().day, 0, 0)
)
abandoned_package_last_commit_10_years = make_aware(
    datetime.datetime(now().year - 10, now().month, now().day, 0, 0)
)
active_package_last_commit = now() - timedelta(minutes=30)


def load():
    category, created = Category.objects.get_or_create(
        pk=2,
        description="Large efforts that combine many python modules or apps. Examples include Django, Pinax, and Satchmo. Most CMS falls into this category.",
        show_pypi=True,
        title_plural="Frameworks",
        title="Framework",
        slug="frameworks",
    )

    package, created = Package.objects.get_or_create(
        pk=6,
        category=category,
        title="Django CMS",
        created_by=None,
        repo_watchers=967,
        pypi_url="https://pypi.org/project/django-cms/",
        pypi_downloads=26257,
        last_modified_by=None,
        repo_url="https://github.com/divio/django-cms",
        participants="chrisglass,digi604,erobit,fivethreeo,ojii,stefanfoulis,pcicman,DrMeers,brightwhitefox,FlashJunior,philomat,jezdez,havan,acdha,m000,hedberg,piquadrat,spookylukey,izimobil,ulope,emiquelito,aaloy,lasarux,yohanboniface,aparo,jsma,johbo,ionelmc,quattromic,almost,specialunderwear,mitar,yml,pajusmar,diofeher,marcor,cortextual,hysia,dstufft,ssteinerx,oversize,jalaziz,tercerojista,eallik,f4nt,kaapa,mbrochh,srj55,dz,mathijs-dumon,sealibora,cyberj,adsworth,tokibito,DaNmarner,IanLewis,indexofire,bneijt,tehfink,PPvG,seyhunak,pigletto,fcurella,gleb-chipiga,beshrkayali,kinea,lucasvo,jordanjambazov,tonnzor,centralniak,arthur-debert,bzed,jasondavies,nimnull,limpbrains,pvanderlinden,sleytr,sublimevelo,netpastor,dtt101,fkazimierczak,merlex,mrlundis,restless,eged,shanx,ptoal",
        # usage=[129, 50, 43, 183, 87, 204, 1, 231, 233, 239, 241, 248, 252, 262, 263, 268, 282, 284, 298, 32, 338, 342, 344, 345, 348, 355, 388, 401, 295, 36, 444, 422, 449, 157, 457, 462, 271, 143, 433, 554, 448, 470, 562, 86, 73, 504, 610, 621, 651, 663, 688, 661, 766, 770, 773, 799, 821, 834, 847, 848, 850, 322, 883, 823, 958, 387, 361, 123, 1026, 516, 715, 1105],
        repo_forks=283,
        slug="django-cms",
        repo_description="An Advanced Django CMS.",
    )
    commit, created = Commit.objects.get_or_create(
        package_id=6,
        commit_date=active_package_last_commit,
        commit_hash="12341234123412341234123412341234",
    )

    package, created = Package.objects.get_or_create(
        pk=7,
        category=category,
        title="Abandoned Package",
        created_by=None,
        repo_watchers=1000,
        pypi_downloads=26257,
        last_modified_by=None,
        repo_url="https://github.com/divio/django-divioadmin",
        repo_forks=1000,
        slug="django-divioadmin",
        repo_description="not maintained anymore.",
    )
    commit, created = Commit.objects.get_or_create(
        package_id=7,
        commit_date=abandoned_package_last_commit,
        commit_hash="2b54b0ae95ef805c07ca3c0b9c5184466b65c55b",
    )

    package, created = Package.objects.get_or_create(
        pk=8,
        category=category,
        title="Abandoned Package 10 years",
        created_by=None,
        repo_watchers=1000,
        pypi_downloads=26257,
        last_modified_by=None,
        repo_url="https://github.com/divio/django-divioadmin2",
        repo_forks=1000,
        slug="django-divioadmin2",
        repo_description="not maintained anymore.",
    )
    commit, created = Commit.objects.get_or_create(
        package_id=8,
        commit_date=abandoned_package_last_commit_10_years,
        commit_hash="2b54b0ae95ef805c07ca3c0b9c5184466b65c66c",
    )

    user, created = User.objects.get_or_create(
        pk=129,
        username="unbracketed",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-08-28 20:48:35",
        # groups=[],
        # user_permissions=[],
        password="sha1$a5c47$0e9be0aee0cb60648a3e0a70f462e0943a46aeab",
        email="brian@unbracketed.com",
        date_joined="2010-08-28 20:47:52",
    )

    user, created = User.objects.get_or_create(
        pk=50,
        username="ojii",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2011-03-09 14:50:02",
        # groups=[],
        # user_permissions=[],
        password="sha1$a7428$563858792ba94c8706db374eed9d2708536ea2a5",
        email="jonas.obrist@divio.ch",
        date_joined="2010-08-18 03:35:23",
    )
    user, created = User.objects.get_or_create(
        pk=43,
        username="vvarp",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-09-29 12:08:01",
        # groups=[],
        # user_permissions=[],
        password="sha1$ed0c0$ec7ed6b92a963fd02cd0e1e1fcd90d66591a29b8",
        email="maciek@id43.net",
        date_joined="2010-08-17 18:43:12",
    )
    user, created = User.objects.get_or_create(
        pk=183,
        username="onjin",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-09-09 07:47:11",
        # groups=[],
        # user_permissions=[],
        password="sha1$1965c$9b8cc38cec3672b515787c227a3ef7ceea2ae785",
        email="onjinx@gmail.com",
        date_joined="2010-09-07 02:23:11",
    )
    user, created = User.objects.get_or_create(
        pk=87,
        username="jezdez",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2011-02-09 09:29:33",
        # groups=[],
        # user_permissions=[],
        password="sha1$97523$0d3cdbbd2930052fe89ebf38ef7267bc85479032",
        email="jannis@leidel.info",
        date_joined="2010-08-21 04:14:03",
    )
    user, created = User.objects.get_or_create(
        pk=204,
        username="flmendes",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-09-14 18:01:16",
        # groups=[],
        # user_permissions=[],
        password="sha1$68ef6$750d02a7c6a1b8d14adb31a8374cb18d6f37708e",
        email="flmendes@gmail.com",
        date_joined="2010-09-08 22:49:34",
    )
    user, created = User.objects.get_or_create(
        pk=1,
        username="audreyr",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=True,
        is_staff=True,
        last_login="2011-03-13 23:44:00",
        # groups=[],
        # user_permissions=[],
        password="sha1$c84c1$dfd3748f63f48e2639d3c4d1caa113acf6bde51f",
        email="audreyr@gmail.com",
        date_joined="2010-08-15 22:15:50",
    )
    user, created = User.objects.get_or_create(
        pk=231,
        username="digi604",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-09-12 07:34:07",
        # groups=[],
        # user_permissions=[],
        password="sha1$0f7f5$523594505138d1182fa413826c02b1e32ee8b95c",
        email="digi@treepy.com",
        date_joined="2010-09-12 07:32:42",
    )
    user, created = User.objects.get_or_create(
        pk=233,
        username="mikl",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-09-12 08:57:34",
        # groups=[],
        # user_permissions=[],
        password="sha1$c4af2$e50af5facac17d8b6cd83e7ccc06dee27e33a6a1",
        email="mikkel@hoegh.org",
        date_joined="2010-09-12 08:56:36",
    )
    user, created = User.objects.get_or_create(
        pk=239,
        username="arthurk",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-09-12 19:13:47",
        # groups=[],
        # user_permissions=[],
        password="sha1$dbc73$f0d8c4476121c8a66fae45f7131db9df71e9aab4",
        email="arthur@arthurkoziel.com",
        date_joined="2010-09-12 19:12:55",
    )
    user, created = User.objects.get_or_create(
        pk=241,
        username="juacompe",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-09-13 03:23:21",
        # groups=[],
        # user_permissions=[],
        password="sha1$d08ef$4f9c0272cafe2ce6b5619c79f8ecf7f6dd3c024e",
        email="juacompe@gmail.com",
        date_joined="2010-09-13 03:10:39",
    )
    user, created = User.objects.get_or_create(
        pk=248,
        username="kocakafa",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-09-13 10:09:36",
        # groups=[],
        # user_permissions=[],
        password="sha1$624bd$101a762ea78432c4a4c25c3a4f2558e14126b0d5",
        email="cemrekutluay@gmail.com",
        date_joined="2010-09-13 10:08:40",
    )
    user, created = User.objects.get_or_create(
        pk=252,
        username="dmoisset",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-11-09 09:21:27",
        # groups=[],
        # user_permissions=[],
        password="sha1$0b205$20bbdba061603ed658ef772d360dd30f34b6aad6",
        email="dmoisset@machinalis.com",
        date_joined="2010-09-13 13:53:32",
    )
    user, created = User.objects.get_or_create(
        pk=262,
        username="eged",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-10-06 04:22:27",
        # groups=[],
        # user_permissions=[],
        password="sha1$b81b9$76327ae4d11587d816a7dc0da89b71c2e36be73d",
        email="viliam.segeda@gmail.com",
        date_joined="2010-09-14 06:50:44",
    )
    user, created = User.objects.get_or_create(
        pk=263,
        username="rtpm",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-09-14 07:48:22",
        # groups=[],
        # user_permissions=[],
        password="sha1$7d578$d69bb08ff132271fa1725245ec79dfb8296a0a4b",
        email="rtpm@gazeta.pl",
        date_joined="2010-09-14 07:47:29",
    )
    user, created = User.objects.get_or_create(
        pk=268,
        username="flynnguy",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-09-14 09:21:21",
        # groups=[],
        # user_permissions=[],
        password="sha1$615f8$2286dc5ce690fcd70ebc796f7ffd9742a0fbce8e",
        email="chris@flynnguy.com",
        date_joined="2010-09-14 09:20:08",
    )
    user, created = User.objects.get_or_create(
        pk=282,
        username="mcosta",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-09-14 18:41:59",
        # groups=[],
        # user_permissions=[],
        password="sha1$7a4e1$8f37adee1eaa107354d0400cfbd7e7a678506aa9",
        email="m.costacano@gmail.com",
        date_joined="2010-09-14 18:41:02",
    )
    user, created = User.objects.get_or_create(
        pk=284,
        username="chromano",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-10-13 12:50:44",
        # groups=[],
        # user_permissions=[],
        password="sha1$7c7b3$5c009b3002d04f2ef3db01a17501f8d852a8e3ee",
        email="chromano@gmail.com",
        date_joined="2010-09-14 19:30:41",
    )
    user, created = User.objects.get_or_create(
        pk=298,
        username="robedwards",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-09-15 07:50:34",
        # groups=[],
        # user_permissions=[],
        password="sha1$cc020$29594e7501c4697ba86c8ff0698f7d5eaf16ff14",
        email="rob@brycefarrah.com",
        date_joined="2010-09-15 07:42:18",
    )
    user, created = User.objects.get_or_create(
        pk=32,
        username="markusgattol",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2011-01-07 04:14:45",
        # groups=[],
        # user_permissions=[],
        password="sha1$289e4$fb00c9de77f991b423ba91edcd91f14ab91afcd7",
        email="markus.gattol@sunoano.org",
        date_joined="2010-08-17 14:05:10",
    )
    user, created = User.objects.get_or_create(
        pk=338,
        username="iamsk",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-09-17 04:26:17",
        # groups=[],
        # user_permissions=[],
        password="sha1$7f703$cf45848f28e30adfee3a30cc329e66a14d25bbce",
        email="iamsk.info@gmail.com",
        date_joined="2010-09-17 04:14:36",
    )
    user, created = User.objects.get_or_create(
        pk=342,
        username="kiello",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-09-17 05:40:20",
        # groups=[],
        # user_permissions=[],
        password="sha1$72adc$31bd0fc2440d9ded4b816e6812165f3565801807",
        email="mauro.doglio@gmail.com",
        date_joined="2010-09-17 05:39:00",
    )
    user, created = User.objects.get_or_create(
        pk=344,
        username="nimnull",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-09-17 07:32:43",
        # groups=[],
        # user_permissions=[],
        password="sha1$08b73$b8c7e885cffcc351540dbae0b5d35cdf3123a3c2",
        email="nimnull@gmail.com",
        date_joined="2010-09-17 07:31:45",
    )
    user, created = User.objects.get_or_create(
        pk=345,
        username="dblkey",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-09-17 08:17:44",
        # groups=[],
        # user_permissions=[],
        password="sha1$1f412$5c7a8e402e0f9e588632d6662ec6da3029eaf72f",
        email="thedoublekey@gmail.com",
        date_joined="2010-09-17 08:16:44",
    )
    user, created = User.objects.get_or_create(
        pk=348,
        username="netpastor",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-09-17 10:18:34",
        # groups=[],
        # user_permissions=[],
        password="sha1$9971f$cffb9546d3f399a0c6e7f34ad57144e8c9a66b32",
        email="vadimshatalov@yandex.ru",
        date_joined="2010-09-17 10:17:26",
    )
    user, created = User.objects.get_or_create(
        pk=355,
        username="limpbrains",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-09-17 17:45:01",
        # groups=[],
        # user_permissions=[],
        password="sha1$d521e$ac48433870ff69fbbdf8e67b6d5b9341b3f70565",
        email="limpbrains@mail.ru",
        date_joined="2010-09-17 17:43:45",
    )
    user, created = User.objects.get_or_create(
        pk=388,
        username="mrbox",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-11-18 13:01:33",
        # groups=[],
        # user_permissions=[],
        password="sha1$c34a1$c228bbe096cd1cce6f6121aa3502f88a3df271a1",
        email="jakub@paczkowski.eu",
        date_joined="2010-09-21 09:20:54",
    )
    user, created = User.objects.get_or_create(
        pk=401,
        username="archatas",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-10-14 12:54:28",
        # groups=[],
        # user_permissions=[],
        password="sha1$42d2e$39b36644f6246297e77af51837d898bd784b62ff",
        email="aidasbend@yahoo.com",
        date_joined="2010-09-21 23:45:16",
    )
    user, created = User.objects.get_or_create(
        pk=295,
        username="mat",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-09-15 07:49:20",
        # groups=[],
        # user_permissions=[],
        password="sha1$2cb8b$09abc15052a91cd123c32f1a3cd1402a3f5759bf",
        email="mat@apinc.org",
        date_joined="2010-09-15 07:08:21",
    )
    user, created = User.objects.get_or_create(
        pk=36,
        username="joshourisman",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2011-02-11 08:41:47",
        # groups=[],
        # user_permissions=[],
        password="sha1$8a414$44a1517f3443f3c2094d760fcf10c06ac6fca38f",
        email="josh@joshourisman.com",
        date_joined="2010-08-17 14:53:18",
    )
    user, created = User.objects.get_or_create(
        pk=444,
        username="piquadrat",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-09-28 04:51:17",
        # groups=[],
        # user_permissions=[],
        password="sha1$e048a$fc0ea2dc56c3ec7a4ea3c2af981d0e5633f0a1b6",
        email="piquadrat@gmail.com",
        date_joined="2010-09-28 04:49:14",
    )
    user, created = User.objects.get_or_create(
        pk=422,
        username="evotech",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2011-03-05 11:33:42",
        # groups=[],
        # user_permissions=[],
        password="sha1$c4056$24151ba166330bc8a113432f35d549bec8e603de",
        email="ivzak@yandex.ru",
        date_joined="2010-09-24 05:41:49",
    )
    user, created = User.objects.get_or_create(
        pk=449,
        username="partizan",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-09-28 17:58:49",
        # groups=[],
        # user_permissions=[],
        password="sha1$c5658$5738a1688c1ed065eeda86eed5441b4a3f564dff",
        email="psychotechnik@gmail.com",
        date_joined="2010-09-28 13:03:59",
    )
    user, created = User.objects.get_or_create(
        pk=157,
        username="feuervogel",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-10-21 07:46:40",
        # groups=[],
        # user_permissions=[],
        password="sha1$b62ba$b0002edb8ce814228b3812112f2878d44dd880ee",
        email="jumo@gmx.de",
        date_joined="2010-08-31 13:47:05",
    )
    user, created = User.objects.get_or_create(
        pk=457,
        username="LukaszDziedzia",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-11-30 05:44:58",
        # groups=[],
        # user_permissions=[],
        password="sha1$651bc$71ea97a3322ea5720884654a6fa360f415fca698",
        email="l.dziedzia@gmail.com",
        date_joined="2010-09-29 07:43:26",
    )
    user, created = User.objects.get_or_create(
        pk=462,
        username="emencia",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-11-15 16:25:23",
        # groups=[],
        # user_permissions=[],
        password="sha1$28466$0cd6b9fbb628c2837c0e4dcdc3e433aed1174ead",
        email="roger@emencia.com",
        date_joined="2010-09-29 12:00:32",
    )
    user, created = User.objects.get_or_create(
        pk=271,
        username="zenweasel",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-11-10 22:41:53",
        # groups=[],
        # user_permissions=[],
        password="sha1$705e8$5759884e7222e061d08de3cbff31b53b068fd266",
        email="brent@thebuddhalodge.com",
        date_joined="2010-09-14 11:35:25",
    )
    user, created = User.objects.get_or_create(
        pk=143,
        username="spookylukey",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2011-02-19 17:09:12",
        # groups=[],
        # user_permissions=[],
        password="sha1$70e5d$50c6a37cbac336cf1a08f4672bfa2002b4d2a55f",
        email="L.Plant.98@cantab.net",
        date_joined="2010-08-30 08:33:49",
    )
    user, created = User.objects.get_or_create(
        pk=433,
        username="avoine",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-12-03 10:57:01",
        # groups=[],
        # user_permissions=[],
        password="sha1$9d041$240309830d9ca972b2dc2fe24158e01ee7ba4a9d",
        email="patrick@koumbit.org",
        date_joined="2010-09-26 16:31:53",
    )
    user, created = User.objects.get_or_create(
        pk=554,
        username="ethan",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-12-15 15:59:39",
        # groups=[],
        # user_permissions=[],
        password="sha1$92dd1$37703fa27808c902fcd58792936afe41c02a70d0",
        email="Ethan.Leland@gmail.com",
        date_joined="2010-10-20 18:23:30",
    )
    user, created = User.objects.get_or_create(
        pk=448,
        username="chem",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-12-23 11:47:50",
        # groups=[],
        # user_permissions=[],
        password="sha1$f45bb$40332f58b55706b6f6059f855b18b3cd588b8948",
        email="chemt@ukr.net",
        date_joined="2010-09-28 11:36:56",
    )
    user, created = User.objects.get_or_create(
        pk=470,
        username="wires",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-09-30 10:26:07",
        # groups=[],
        # user_permissions=[],
        password="sha1$e15d5$a18fc4b6f8b628cc6fb6ae0d8133a423e9ad1d1e",
        email="jelle@defekt.nl",
        date_joined="2010-09-30 10:20:20",
    )
    user, created = User.objects.get_or_create(
        pk=562,
        username="rasca",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2011-01-06 11:59:42",
        # groups=[],
        # user_permissions=[],
        password="sha1$edd41$bd2c72f9c2c2b59aac5775bbc59d4b529494aabf",
        email="rasca7@hotmail.com",
        date_joined="2010-10-24 12:24:08",
    )
    user, created = User.objects.get_or_create(
        pk=86,
        username="justhamade",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2011-03-06 18:57:20",
        # groups=[],
        # user_permissions=[],
        password="sha1$b7a5a$53b2cb1cd3c20a2cee79b170b56ea88ec73d9685",
        email="justhamade@gmail.com",
        date_joined="2010-08-21 00:11:33",
    )
    user, created = User.objects.get_or_create(
        pk=73,
        username="slav0nic",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2011-03-13 16:46:13",
        # groups=[],
        # user_permissions=[],
        password="sha1$13d6f$fafddd832ac31aff59ec6ff155e4d5284e675c56",
        email="slav0nic0@gmail.com",
        date_joined="2010-08-19 06:24:12",
    )
    user, created = User.objects.get_or_create(
        pk=504,
        username="Fantomas42",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2011-03-02 08:55:17",
        # groups=[],
        # user_permissions=[],
        password="sha1$1166e$cc6971b2eb92eeed5ea0d43f896dcc46a47102eb",
        email="fantomas42@gmail.com",
        date_joined="2010-10-07 09:26:41",
    )
    user, created = User.objects.get_or_create(
        pk=610,
        username="globalnamespace",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-11-04 13:38:34",
        # groups=[],
        # user_permissions=[],
        password="sha1$d3fbf$f3a1fc7fe6ca203ace449497d437cf06c67e905d",
        email="mbest@pendragon.org",
        date_joined="2010-11-04 13:37:57",
    )
    user, created = User.objects.get_or_create(
        pk=621,
        username="btubbs",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-11-06 19:45:21",
        # groups=[],
        # user_permissions=[],
        password="sha1$6ebe8$04ff06448cbf632a9d54f13e7d3c5b808e08b528",
        email="brent.tubbs@gmail.com",
        date_joined="2010-11-06 19:36:22",
    )
    user, created = User.objects.get_or_create(
        pk=651,
        username="HounD",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-11-15 16:02:52",
        # groups=[],
        # user_permissions=[],
        password="sha1$e5fc1$0ad97a61ed9bb34904e9df36ba4bbb4eca7c35c9",
        email="vladshikhov@gmail.com",
        date_joined="2010-11-13 00:45:44",
    )
    user, created = User.objects.get_or_create(
        pk=663,
        username="encinas",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-11-15 10:11:00",
        # groups=[],
        # user_permissions=[],
        password="sha1$900ea$2044dfec30282981ce4094db6a0c7f1d9bba0ca9",
        email="list@encinas-fernandez.eu",
        date_joined="2010-11-15 10:05:27",
    )
    user, created = User.objects.get_or_create(
        pk=688,
        username="nasp",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-11-20 22:31:48",
        # groups=[],
        # user_permissions=[],
        password="sha1$ed6f2$964b18357a346a3063ab299fbe34f38268aaf41f",
        email="charette.s@gmail.com",
        date_joined="2010-11-20 22:27:37",
    )
    user, created = User.objects.get_or_create(
        pk=661,
        username="ralphleyga",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2011-03-11 04:32:15",
        # groups=[],
        # user_permissions=[],
        password="sha1$52255$9263926740de1d194152697f9f9da2466b547ce4",
        email="ralphfleyga@gmail.com",
        date_joined="2010-11-15 08:46:31",
    )
    user, created = User.objects.get_or_create(
        pk=766,
        username="xigit",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-12-06 04:28:14",
        # groups=[],
        # user_permissions=[],
        password="sha1$917d2$cbead9bd51c7b47651e92dfd315485a054794187",
        email="xigitech@gmail.com",
        date_joined="2010-12-06 04:26:04",
    )
    user, created = User.objects.get_or_create(
        pk=770,
        username="espenhogbakk",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-12-06 06:13:29",
        # groups=[],
        # user_permissions=[],
        password="sha1$e354e$d7c7d6cf7a80f6ccd6e96c688362e5e55a651b62",
        email="espen@hogbakk.no",
        date_joined="2010-12-06 06:12:27",
    )
    user, created = User.objects.get_or_create(
        pk=773,
        username="petko",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-12-06 07:02:29",
        # groups=[],
        # user_permissions=[],
        password="sha1$86046$91b8739ec7172f6381ae9827a16745084ac960d8",
        email="petko@magicbg.com",
        date_joined="2010-12-06 07:01:57",
    )
    user, created = User.objects.get_or_create(
        pk=799,
        username="eallik",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-12-06 12:49:19",
        # groups=[],
        # user_permissions=[],
        password="sha1$601f6$e0a658e028c87227715b617f31c4c04f479daf0f",
        email="eallik+djangopackages@gmail.com",
        date_joined="2010-12-06 12:47:55",
    )
    user, created = User.objects.get_or_create(
        pk=821,
        username="digitaldreamer",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-12-09 23:39:29",
        # groups=[],
        # user_permissions=[],
        password="sha1$920b7$590a350f467603856b41b302f4dbb3cf76c99f52",
        email="poyzer@gmail.com",
        date_joined="2010-12-09 23:37:03",
    )
    user, created = User.objects.get_or_create(
        pk=834,
        username="andrey_shipilov",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-12-13 06:56:07",
        # groups=[],
        # user_permissions=[],
        password="sha1$59dc2$e720ca75bb1e1aeb66b50a716b74428955c86122",
        email="tezro.gb@gmail.com",
        date_joined="2010-12-13 06:54:28",
    )
    user, created = User.objects.get_or_create(
        pk=847,
        username="john",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-12-15 23:10:14",
        # groups=[],
        # user_permissions=[],
        password="sha1$fa281$87df6e12a569a9383986d0047f36e54a93d0812c",
        email="xjh8619kl93@163.com",
        date_joined="2010-12-15 23:01:23",
    )
    user, created = User.objects.get_or_create(
        pk=848,
        username="tmilovan",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-12-16 13:03:30",
        # groups=[],
        # user_permissions=[],
        password="sha1$a2979$2c86ec53cd382a822ff4ac9764e2f65bd8d7e7c9",
        email="tmilovan@fwd.hr",
        date_joined="2010-12-16 13:02:12",
    )
    user, created = User.objects.get_or_create(
        pk=850,
        username="silvergeko",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-12-17 15:22:38",
        # groups=[],
        # user_permissions=[],
        password="sha1$c9c20$7b4cf6b907147e30a105360888ac4a903ba782ab",
        email="scopel.emanuele@gmail.com",
        date_joined="2010-12-17 15:21:25",
    )
    user, created = User.objects.get_or_create(
        pk=322,
        username="tino",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-12-21 06:01:06",
        # groups=[],
        # user_permissions=[],
        password="sha1$3cb5f$36e621a1d7d38a9159e9e7bc86cd93f0636d330d",
        email="tinodb@gmail.com",
        date_joined="2010-09-16 16:27:02",
    )
    user, created = User.objects.get_or_create(
        pk=883,
        username="mariocesar",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2010-12-29 08:36:45",
        # groups=[],
        # user_permissions=[],
        password="sha1$705d5$63af6bfa8f27b759b755574f6c7d8158d240c526",
        email="mariocesar.c50@gmail.com",
        date_joined="2010-12-29 08:35:49",
    )
    user, created = User.objects.get_or_create(
        pk=823,
        username="qrilka",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2011-01-19 17:17:17",
        # groups=[],
        # user_permissions=[],
        password="sha1$37911$f2622929d7f460a9a4d6204325b1349940aafe83",
        email="qrilka@gmail.com",
        date_joined="2010-12-10 05:15:35",
    )
    user, created = User.objects.get_or_create(
        pk=958,
        username="dmpeters63",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2011-01-28 03:06:30",
        # groups=[],
        # user_permissions=[],
        password="sha1$66668$0eb23655452720bdb2e2ff8874bd84d5ae599dfb",
        email="dmpeters63@gmail.com",
        date_joined="2011-01-28 03:04:11",
    )
    user, created = User.objects.get_or_create(
        pk=387,
        username="oversize",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2011-01-28 07:37:47",
        # groups=[],
        # user_permissions=[],
        password="sha1$f291f$d08c5869b9dafc8a61c460599e4c2519f3e60cda",
        email="manuel@schmidtman.de",
        date_joined="2010-09-21 05:44:08",
    )
    user, created = User.objects.get_or_create(
        pk=361,
        username="moskrc",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2011-03-05 04:35:45",
        # groups=[],
        # user_permissions=[],
        password="sha1$3627b$3a2d7e40c2adb5f6fe459737e1c6abfc242b225c",
        email="moskrc@gmail.com",
        date_joined="2010-09-18 15:53:47",
    )
    user, created = User.objects.get_or_create(
        pk=123,
        username="stefanfoulis",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2011-02-21 03:18:48",
        # groups=[],
        # user_permissions=[],
        password="sha1$8ef17$5559490fac93e0e40ac637e84b3c8069d2091879",
        email="stefan.foulis@gmail.com",
        date_joined="2010-08-28 13:54:39",
    )
    user, created = User.objects.get_or_create(
        pk=1026,
        username="gmh04",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2011-03-14 16:02:05",
        # groups=[],
        # user_permissions=[],
        password="sha1$d82a2$96d68a17ce55446037d67b3cf076f5e47cca1718",
        email="gmh04@netscape.net",
        date_joined="2011-02-16 16:05:47",
    )
    user, created = User.objects.get_or_create(
        pk=516,
        username="azizmb",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2011-02-25 13:20:16",
        # groups=[],
        # user_permissions=[],
        password="sha1$dd3cb$321edb091caa16a8fd2231dfc61bbb27ecc455eb",
        email="aziz.mansur@gmail.com",
        date_joined="2010-10-09 13:54:45",
    )
    user, created = User.objects.get_or_create(
        pk=715,
        username="mwalling",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2011-03-02 16:57:24",
        # groups=[],
        # user_permissions=[],
        password="sha1$114c6$195ee166ab51a5727641915fe4bc822d1ba9052f",
        email="mark@markwalling.org",
        date_joined="2010-11-28 13:36:12",
    )
    user, created = User.objects.get_or_create(
        pk=1105,
        username="evilkarlothian",
        first_name="",
        last_name="",
        is_active=True,
        is_superuser=False,
        is_staff=False,
        last_login="2011-03-14 18:54:25",
        # groups=[],
        # user_permissions=[],
        password="sha1$e509f$a44e555f6c7aee67fde34dbe995fce20a4af2b96",
        email="karlbowden@gmail.com",
        date_joined="2011-03-14 18:52:34",
    )

    cms_package = Package.objects.get(pk=6)

    version, created = Version.objects.get_or_create(
        pk=9,
        license="BSD License",
        downloads=13644,
        package=cms_package,
        number="2.1.0.beta3",
        hidden=False,
        supports_python3=True,
    )
    version, created = Version.objects.get_or_create(
        pk=10,
        license="BSD License",
        downloads=4326,
        package=cms_package,
        number="2.0.2",
        hidden=False,
    )
    version, created = Version.objects.get_or_create(
        pk=11,
        license="BSD License",
        downloads=212,
        package=cms_package,
        number="2.0.1",
        hidden=False,
    )
    version, created = Version.objects.get_or_create(
        pk=12,
        license="BSD License",
        downloads=1062,
        package=cms_package,
        number="2.0.0",
        hidden=False,
    )
    version, created = Version.objects.get_or_create(
        pk=1870,
        license="BSD License",
        downloads=299,
        package=cms_package,
        number="2.1.0.rc1",
        hidden=False,
    )
    version, created = Version.objects.get_or_create(
        pk=1913,
        license="BSD License",
        downloads=726,
        package=cms_package,
        number="2.1.0.rc2",
        hidden=False,
    )
    version, created = Version.objects.get_or_create(
        pk=1977,
        license="BSD License",
        downloads=850,
        package=cms_package,
        number="2.1.0.rc3",
        hidden=False,
    )
    version, created = Version.objects.get_or_create(
        pk=2041,
        license="BSD License",
        downloads=1613,
        package=cms_package,
        number="2.1.0",
        hidden=False,
    )
    version, created = Version.objects.get_or_create(
        pk=2177,
        license="BSD License",
        downloads=906,
        package=cms_package,
        number="2.1.1",
        hidden=False,
    )
    version, created = Version.objects.get_or_create(
        pk=2252,
        license="BSD License",
        downloads=715,
        package=cms_package,
        number="2.1.2",
        hidden=False,
    )
    version, created = Version.objects.get_or_create(
        pk=2278,
        license="BSD License",
        downloads=1904,
        package=cms_package,
        number="2.1.3",
        hidden=False,
    )
