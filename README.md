# Program to scrape news from Web.

## Description

This program intends to grab news from first two pages of Hacker News Website(<https://news.ycombinator.com/>) with more than 100 points.

## Requirements

Please find below the requirements to run this project:

- Python 3
- Modules - requests, beautifulsoup4, pprint[Built-in]

## Usage

1.Install modules using the command:

```
pip install requests
```

2.Run the [Python file](scrape.py):

```
python scrape.py
```

3.The expected output format is shown below.

```
[{'link': 'https://twitter.com/tubetimeus/status/1306359385656946688',
  'title': 'This electrical transmission tower has a problem',
  'votes': 1634},
 {'link': 'https://www.journals.uchicago.edu/doi/abs/10.1086/691462?journalCode=jacr',
  'title': 'The Presence of One’s Own Smartphone Reduces Available Cognitive '
           'Capacity (2017)',
  'votes': 818},
 {'link': 'https://bugzilla.mozilla.org/show_bug.cgi?id=22687',
  'title': '21 years after the request OpenPGP support gets added to '
           'Thunderbird',
  'votes': 673},
 {'link': 'https://github.com/raspberrypi/rpi-eeprom/issues/28',
  'title': 'Raspberry Pi 4 can finally boot directly from USB',
  'votes': 633},
 {'link': 'https://github.com/FreeCAD/FreeCAD',
  'title': 'FreeCAD: A free and open source multiplatform 3D parametric '
           'modeler',
  'votes': 590},
 {'link': 'https://changelog.com/posts/use-long-flags-when-scripting',
  'title': 'Use long flags when scripting (2013)',
  'votes': 443},
 {'link': 'https://github.com/mrDIMAS/rg3d',
  'title': 'rg3d: Rust 3D game engine with an FPS demo game and scene editor',
  'votes': 384},
 {'link': 'https://www.bunniestudios.com/blog/?p=5921',
  'title': 'Precursor – A mobile, open source electronics platform',
  'votes': 369},
 {'link': 'https://www.cisa.gov/blog/2020/09/18/windows-server-vulnerability-requires-immediate-attention',
  'title': 'Windows Server vulnerability requires immediate attention',
  'votes': 321},
 {'link': 'https://www.cinemablend.com/news/2546992/why-christopher-nolan-actually-blew-up-a-real-plane-for-tenet',
  'title': 'It was more efficient to blow up a real 747 than to use miniatures '
           'or CGI',
  'votes': 299},
 {'link': 'https://dissenter.substack.com/p/khaled-el-masri-survivor-of-cia-torture',
  'title': 'Survivor of CIA Torture and Rendition Supports Assange at '
           'Extradition Trial',
  'votes': 271},
 {'link': 'https://www.justice.gov/usao-wdwa/pr/six-indicted-connection-multi-million-dollar-scheme-bribe-amazon-employees-and',
  'title': 'Six indicted in multimillion dollar scheme to bribe Amazon staff',
  'votes': 237},
 {'link': 'https://www.bbc.com/worklife/article/20200910-the-benefits-of-note-taking-by-hand',
  'title': 'The benefits of note-taking by hand',
  'votes': 230},
 {'link': 'https://github.com/NVIDIA/libcudacxx',
  'title': 'Libcu++: Nvidia C++ Standard Library',
  'votes': 200},
 {'link': 'https://www.theverge.com/2020/9/17/21443851/death-ransomware-attack-hospital-germany-cybersecurity',
  'title': 'Woman dies during a ransomware attack on a German hospital',
  'votes': 189},
 {'link': 'https://archive.org/details/OTRR_X_Minus_One_Singles',
  'title': 'X Minus One: 1950s Science Fiction Radio Programs Available to '
           'Listen (2011)',
  'votes': 181},
 {'link': 'https://www.bicycling.com/culture/a33995147/tom-pritchard-bike-mystery/',
  'title': 'The Mystery of Tom Pritchard’s Bike',
  'votes': 179},
 {'link': 'https://github.com/alexdelorenzo/chromecast_mpris',
  'title': 'Show HN: Control Chromecasts from Linux',
  'votes': 164},
 {'link': 'https://bevyengine.org/news/bevy-0-2/',
  'title': 'Bevy 0.2',
  'votes': 160},
 {'link': 'https://shkspr.mobi/blog/2020/09/all-the-jobs-i-didnt-get/',
  'title': 'All the jobs I failed to get',
  'votes': 157},
 {'link': 'https://thewalrus.ca/older-wiser-better-aging-artists-are-at-their-peak/',
  'title': 'Creativity Changes as We Age',
  'votes': 156},
 {'link': 'https://www.extremetech.com/computing/315186-apple-books-tsmcs-entire-5nm-production-capability',
  'title': 'Apple Books TSMC’s Entire 5nm Production Capability',
  'votes': 146},
 {'link': 'https://www.economist.com/graphic-detail/2020/09/19/the-age-old-strategy-of-buying-cheap-shares-is-faltering',
  'title': 'The age-old strategy of buying cheap shares is faltering',
  'votes': 146},
 {'link': 'https://www.annashipman.co.uk/jfdi/meeting-everyone.html',
  'title': 'Meeting everyone on a new team',
  'votes': 139},
 {'link': 'item?id=24527978',
  'title': 'Ask HN: What is it like to be old? What advice would you give to '
           'younger people?',
  'votes': 117},
 {'link': 'https://twisteros.com/index.html',
  'title': 'Twister OS: Make Raspberry Pi Look Like Windows or macOS',
  'votes': 114},
 {'link': 'https://www.washingtonpost.com/travel/2020/09/18/tourist-trash-mail/',
  'title': 'A Thai national park is mailing trash back to tourists',
  'votes': 109},
 {'link': 'https://kb.netgear.com/000062364/GC108P-GC108PP-Firmware-Version-1-0-5-8',
  'title': 'Netgear Firmware Requires Online Registration',
  'votes': 100}]
```

## Future Scope

Use Jenkins to fire script daily and redirect to an index.html webpage!!! Keep learning!!!
