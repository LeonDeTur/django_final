# Flask project seminar

`python 3.12`

# `venv` — Создание виртуальных сред

    Новое в версии 3.3.

> Исходный код: `Lib/venv/`

- `venv `Модуль обеспечивает поддержку для создания облегченных “виртуальных сред” с их собственными каталогами сайтов, 
необязательно изолированными от системных каталогов сайтов. 
- Каждая виртуальная среда имеет свой собственный двоичный 
файл Python (который соответствует версии двоичного файла, использовался для создания этой среды) и может 
иметь свой собственный независимый набор установленных пакетов Python в каталогах своего сайта.

- См. `PEP 405` для получения дополнительной информации о виртуальных средах Python.

Смотрите также Руководство пользователя по упаковке Python: создание и использование виртуальных сред
Создание виртуальных сред
Создание виртуальных сред выполняется путем выполнения команды venv:

`python3 -m venv /path/to/new/virtual/environment`

Выполнение этой команды создает целевой каталог (создавая любые родительские каталоги, которые еще не существуют) и 
помещает `pyvenv.cfg` в него файл с home ключом. Указывающим на установку `Python`, из которой была запущена команда 
(общее имя для целевого каталога - .`venv`). Он также создает bin подкаталог (или `Scripts` в `Windows`), содержащий 
копию / символическую ссылку двоичного файла / двоичных файлов `Python` (в зависимости от платформы или аргументов, 
используемых во время создания среды). Он также создает (изначально пустой) `lib/pythonX.Y/site-packages` подкаталог 
(в `Windows` это `Lib\site-packages`). Если указан существующий каталог, он будет использоваться повторно.

Устарел с версии 3.6:pyvenv был рекомендуемым инструментом для создания виртуальных сред для Python 3.3 и 3.4 и устарел 
в Python 3.6.

Изменено в версии 3.5: venv теперь для создания виртуальных сред рекомендуется использовать.

В Windows вызовите venv команду следующим образом:

`c:\>c:\Python35\python -м venv c:\path\to\myenv`
В качестве альтернативы, если вы настроили `PATH` `PATHEXT` переменные and для вашей установки Python:

`c:\>python -m venv c:\path\to\myenv`

Команда, если она выполняется с-h, покажет доступные параметры:

Использование: `venv [-h] [--system-site-packages] [--символические ссылки | --копии] [--очистить]
 [--upgrade] [--without-pip] [--prompt ПОДСКАЗКА] [--upgrade-deps]
 ENV_DIR [ENV_DIR ...]`

Создает виртуальные среды Python в одном или нескольких целевых каталогах.

Позиционные аргументы:
 `ENV_DIR` Каталог для создания среды.

Необязательные аргументы:
> `-h`, `--help` показать это справочное сообщение и выйти
 `--system-site-packages`

 Предоставьте виртуальной среде доступ к системному
сайту-каталог пакетов.
> --символические ссылки Пытаются использовать символические ссылки, а не копии, когда символические
ссылки не используются по умолчанию для платформы.
>> --копии Пытаются использовать копии, а не символические ссылки, даже если
символические ссылки используются по умолчанию для платформы.

     --очистить Удалить содержимое каталога среды, если оно
    уже существует, перед созданием среды.
     --обновление Обновите каталог среды, чтобы использовать эту версию
Python, предполагая, что Python был обновлен на месте.
 `--without-pip` Пропускает установку или обновление `pip` в виртуальной
среде (по умолчанию `pip` загружается)
 --приглашение `PROMPT` предоставляет альтернативный префикс приглашения для этой
среды.
 --обновление-deps Обновление основных зависимостей: `pip setuptools` до
последней версии в `PyPI`

После создания среды вы можете захотеть активировать ее, например, путем
поиска скрипта `activate` в его каталоге `bin`.
Изменено в версии 3.9: добавлена `--upgrade-deps` возможность обновления `pip + setuptools` до последней версии в `PyPI`

Изменено в версии 3.4: устанавливает `pip` по умолчанию, добавлены параметры `--without-pipи--copies`
Изменено в версии 3.4: в более ранних версиях, если целевой каталог уже существовал, возникала ошибка, если 
`--clear--upgrade` не была указана опция или.

Примечание Хотя символические ссылки поддерживаются в Windows, они не рекомендуются. Особо следует отметить, что двойной
щелчок `python.exe` в проводнике файлов быстро разрешит символическую ссылку и проигнорирует виртуальную среду.
Примечание В Microsoft Windows может потребоваться включить `Activate.ps1` сценарий, установив политику выполнения для 
пользователя. Вы можете сделать это, выполнив следующую команду PowerShell:
PS `C:> Set-ExecutionPolicy -ExecutionPolicy` RemoteSigned -Область CurrentUser

Дополнительные сведения см. в разделе О политиках выполнения.

Созданный `pyvenv.cfg` файл также включает в `include-system-site-packages` себя ключ, для которого установлено true
значение, если venv выполняется с `--system-site-packages` параметром, `false` иначе.

Если `--without-pip` опция не указана, `ensure pip` будет вызываться для начальной загрузки `pip` в виртуальную среду.

Может быть задано несколько путей venv, и в этом случае в соответствии с заданными параметрами на каждом предоставленном
пути будет создана идентичная виртуальная среда.

После создания виртуальной среды ее можно “активировать” с помощью скрипта в двоичном каталоге виртуальной среды. Вызов 
скрипта зависит от платформы (`<venv>` должен быть заменен путем к каталогу, содержащему виртуальную среду):

## Платформа

### Оболочка

Команда для активации виртуальной среды

`POSIX`

`bash/zsh`
```bash
$ source <venv>/bin/activate
```
`fish`
```fish
$ source <venv>/bin/activate.fish
```
csh/tcsh
```csh/tcsh
$ source <venv>/bin/activate.csh
```

`Ядро PowerShell`
```shell
$ <venv>/bin/Activate.ps1
```
Windows

`cmd.exe`
```cmd
C:\> <venv>\Scripts\activate.bat
```
PowerShell
```shell
PS C:\> <venv>\Scripts\Activate.ps1
```

Когда виртуальная среда активна, `VIRTUAL_ENV` переменной среды устанавливается путь к виртуальной среде. Это можно 
использовать, чтобы проверить, выполняется ли он внутри виртуальной среды.

Вам специально не нужно активировать среду; активация просто добавляет двоичный каталог виртуальной среды к вашему пути,
так что `“python”` вызывает интерпретатор `Python` виртуальной среды, и вы можете запускать установленные скрипты без 
необходимости использовать их полный путь. Однако все скрипты, установленные в виртуальной среде, должны быть доступны 
для запуска без ее активации и автоматически запускаться с помощью `Python` виртуальной среды.

Вы можете деактивировать виртуальную среду, введя “деактивировать” в своей оболочке. Точный механизм зависит от 
платформы и является внутренней деталью реализации (обычно используется скрипт или функция оболочки).

Новое в версии 3.4:`fish` и `csh` сценарии активации.

Новое в версии 3.8: сценарии активации `PowerShell`, установленные в `POSIX` для поддержки ядра PowerShell.

Примечание Виртуальная среда - это среда `Python`. В которой интерпретатор `Python`. Библиотеки и скрипты, установленные в 
нем, изолированы от тех, которые установлены в других виртуальных средах. И (по умолчанию) любых библиотек, 
установленных в “системном” `Python`, то есть той, которая установлена как часть вашей операционной системы.
Виртуальная среда - это дерево каталогов, содержащее исполняемые файлы `Python` и другие файлы, которые указывают, 
что это виртуальная среда.

Обычные средства установки, такие как `setuptools` и `pip`, работают с виртуальными средами, как и ожидалось. Другими 
словами, когда виртуальная среда активна, они устанавливают пакеты `Python` в виртуальную среду без необходимости явного
указания сделать это.

Когда виртуальная среда активна (т. Е. Запущен интерпретатор Python виртуальной среды), атрибуты `sys.prefix` и 
`sys.exec_prefix` указывают на базовый каталог виртуальной среды, тогда `sys.base_prefix` как и sys.`base_exec_prefix` 
указывают на установку `Python` в не виртуальной среде, которая использовалась для создания виртуальной среды. Если 
виртуальная среда не активна, то `sys.prefix` это то же `sys.base_prefix` самое, что и и `sys.exec_prefix` то же 
`sys.base_exec_prefix` самое, что и (все они указывают на установку `Python` в не виртуальной среде).

Когда виртуальная среда активна, любые параметры, изменяющие путь установки, будут игнорироваться во всех `distutils` 
файлах конфигурации, чтобы предотвратить непреднамеренную установку проектов за пределами виртуальной среды.

При работе в командной оболочке пользователи могут сделать виртуальную среду активной, запустив `activate` скрипт в 
каталоге исполняемых файлов виртуальной среды (точное имя файла и команда для использования файла зависят от оболочки), 
который добавляет каталог виртуальной среды для исполняемых файлов к переменной `PATH` среды для запущенной оболочки. 
При других обстоятельствах не должно быть необходимости в активации виртуальной среды; скрипты, установленные в 
виртуальных средах, имеют строку “`shebang`”, которая указывает на интерпретатор `Python` виртуальной среды. Это 
означает, что скрипт будет выполняться с этим интерпретатором независимо от значения `PATH`. В Windows обработка строк 
“shebang” поддерживается, если у вас установлен `Python Launcher` для Windows (это было добавлено в Python в 3.3 - см. 
`PEP 397` для получения более подробной информации). Таким образом, двойной щелчок установленного скрипта в окне 
проводника Windows должен запускать скрипт с правильным интерпретатором без необходимости какой-либо ссылки на его 
виртуальную среду `PATH`.

### PIP installations

`pip` поддерживает установку из PyPI, системы управления версиями, локальных проектов и непосредственно из файлов 
дистрибутива.

*Для того чтобы добавить пакеты в requirements.txt*

`pip freeze > requirements.txt`

*Для того чтобы установить пакеты из requirements.txt, необходимо открыть командную строку, перейти в каталог проекта и 
ввести следующую команду:*

`pip install -r requirements.txt`