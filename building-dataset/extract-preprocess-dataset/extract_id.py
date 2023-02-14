import json
import re
import string

KEY = "tid"

data = """
[
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "companies act 1956",
            "formInput": "companies%20act%201956"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "delhi",
            "formInput": "MVD%20Act+doctypes:delhi",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "R Easwar",
            "formInput": "MVD%20Act+author:R Easwar"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2015,
            "formInput": "MVD%20Act+fromdate:1-1-2015+todate:31-12-2015"
          }
        ]
      ]
    ],
    "docs": [
      {
        "title": "Royal Sundaram Alliance ... vs Raja on 2 February, 2015",
        "covertitles": [],
        "numcites": 1,
        "numcitedby": 0,
        "url": "https://www.mhc.tn.gov.in/judis/index.php/casestatus/viewpdf/577070",
        "headline": " Madras High Court \n Royal Sundaram Alliance ... vs Raja on 2 February, 2015                                                                      CMA.No.1579",
        "docsize": 24716,
        "tid": 116127183,
        "covertids": [],
        "doctype": 24,
        "publishdate": "2015-02-02",
        "firstname": None,
        "secondname": None,
        "lastname": None,
        "fragment": True,
        "docsource": "Madras High Court",
        "covers": []
      },
      {
        "title": "Royal Sundaram Alliance ... vs Raja on 2 February, 2015",
        "covertitles": [],
        "numcites": 1,
        "numcitedby": 0,
        "url": "https://www.mhc.tn.gov.in/judis/index.php/casestatus/viewpdf/612515",
        "headline": " Madras High Court \n Royal Sundaram Alliance ... vs Raja on 2 February, 2015                                                                      CMA.No.1579",
        "docsize": 24479,
        "tid": 113214347,
        "covertids": [],
        "doctype": 24,
        "publishdate": "2015-02-02",
        "firstname": None,
        "secondname": None,
        "lastname": None,
        "fragment": True,
        "docsource": "Madras High Court",
        "covers": []
      },
      {
        "title": "Bilal Ahmad Lone vs Bajaj Allianz General Insu. Co. & ... on 2 December, 2021",
        "covertitles": [],
        "numcites": 1,
        "numcitedby": 0,
        "url": "https://services.ecourts.gov.in/ecourtindiaHC/cases/display_pdf.php?filename=eISc8sUCYnQFBVP%2BVeJCOK%2B3tS%2BCjK8hA%2B%2FRqIfFJJKGff%2FKIK5xkNK%2Fs%2BbcPltV&caseno=CMAM%2F20%2F2017&cCode=2&appFlag=",
        "headline": " Jammu & Kashmir High Court - Srinagar Bench \n Bilal Ahmad Lone vs Bajaj Allianz General Insu. Co",
        "docsize": 8193,
        "tid": 175002022,
        "covertids": [],
        "doctype": 46,
        "publishdate": "2021-12-02",
        "firstname": None,
        "secondname": None,
        "lastname": None,
        "fragment": True,
        "docsource": "Jammu & Kashmir High Court - Srinagar Bench",
        "covers": []
      },
      {
        "title": "K.I.Shanavas vs The Joint Regional Transport ... on 25 March, 2021",
        "covertitles": [],
        "numcites": 0,
        "numcitedby": 0,
        "url": "https://services.ecourts.gov.in/ecourtindiaHC/cases/display_pdf.php?filename=QnBUxJ6a3gIx%2B5SFrUiAoMyFhfUy3mTc0FP81Irn9d6jhYaDp7ixqFqI7qmstU3C&caseno=WP%28C%29%2F3237%2F2021&cCode=1&appFlag=",
        "headline": " Kerala High Court \n K.I.Shanavas vs The Joint Regional Transport ... on 25 March, 2021",
        "docsize": 10227,
        "tid": 124097161,
        "covertids": [],
        "doctype": 30,
        "publishdate": "2021-03-25",
        "firstname": None,
        "secondname": None,
        "lastname": None,
        "fragment": True,
        "docsource": "Kerala High Court",
        "covers": []
      },
      {
        "title": "New India Assurance Co. Ltd. vs Smt. Kamla Singhal And Others on 1 August, 2022",
        "covertitles": [],
        "numcites": 4,
        "numcitedby": 0,
        "url": "https://elegalix.allahabadhighcourt.in/elegalix/WebShowJudgment.do?judgmentID=9691154",
        "headline": " Allahabad High Court \n New India Assurance Co. Ltd. vs Smt. Kamla Singhal And Others on",
        "docsize": 12996,
        "tid": 177926680,
        "covertids": [],
        "doctype": 25,
        "publishdate": "2022-08-01",
        "firstname": None,
        "secondname": None,
        "lastname": None,
        "fragment": True,
        "docsource": "Allahabad High Court",
        "covers": []
      },
      {
        "title": "National Insurance Co. Ltd vs Mst. Hajira And Others on 6 September, 2021",
        "covertitles": [],
        "numcites": 2,
        "numcitedby": 0,
        "url": "https://services.ecourts.gov.in/ecourtindiaHC/cases/display_pdf.php?filename=rC8SUFuyEFsvB5V61cXUrEq9GAEWbU2ccgovu4eLOerZoVK8b88bc56RYIZ7z9wn&caseno=MA%2F87%2F2018&cCode=2&appFlag=",
        "headline": " Jammu & Kashmir High Court - Srinagar Bench \n National Insurance Co. Ltd vs Mst. Hajira And Others",
        "docsize": 13463,
        "tid": 174013085,
        "covertids": [],
        "doctype": 46,
        "publishdate": "2021-09-06",
        "firstname": None,
        "secondname": None,
        "lastname": None,
        "fragment": True,
        "docsource": "Jammu & Kashmir High Court - Srinagar Bench",
        "covers": []
      },
      {
        "title": "National Insurance Company Ltd vs Pankaj Bhardwaj & Ors on 4 June, 2019",
        "covertitles": [],
        "numcites": 1,
        "numcitedby": 0,
        "url": "http://services.ecourts.gov.in/ecourtindiaHC/cases/display_pdf.php?filename=oo%2BtRJJeFk03ErxBsOJjIFqtPD%2Bc4%2B%2F5lNezCXrnPP8uvbhA4mJ1xyx5ViNkHdIt&caseno=MA%2F660%2F2010&cCode=1&appFlag=",
        "headline": "Kumar who produced record of original license No.\n\n354/<b>MVD</b> and stated that no such license was issued in favor ... held that 'under the  Motor Vehicles <b>Act</b> , holding of a valid driving\n\nlicence is one of the conditions of contract",
        "docsize": 10580,
        "tid": 146481012,
        "covertids": [],
        "doctype": 29,
        "publishdate": "2019-06-04",
        "firstname": None,
        "secondname": None,
        "lastname": None,
        "fragment": True,
        "docsource": "Jammu & Kashmir High Court",
        "covers": []
      },
      {
        "title": "Suo Motu vs State Of Kerala on 28 June, 2022",
        "covertitles": [],
        "numcites": 0,
        "numcitedby": 0,
        "url": "https://hckinfo.kerala.gov.in/digicourt/orders/2021/213900000202021_11.pdf",
        "headline": "respondent\n\nTransport    Commissioner         (tcoffice.<b>mvd</b>@kerala.gov.in/tc.<b>mvd</b>@\n\nkerala.gov.in)       and   the   3rd   respondent   State   Police   Chief ... Motor Vehicles Department\n                                    5 \nSSCR No.20 of 2021\n\n\n\n<b>acting</b> against contract carriages using unauthorised lights and\n\nsound system that",
        "docsize": 6032,
        "tid": 114118747,
        "covertids": [],
        "doctype": 30,
        "publishdate": "2022-06-28",
        "firstname": None,
        "secondname": None,
        "lastname": None,
        "fragment": True,
        "docsource": "Kerala High Court",
        "covers": []
      },
      {
        "title": "Esha Sajgotra vs <b>Mvd</b> University on 10 February, 2011",
        "covertitles": [],
        "numcites": 4,
        "numcitedby": 0,
        "url": "http://164.100.72.12/ncdrcrep/judgement/110110427125831421Esha%20Sajgotra.htm",
        "headline": " State Consumer Disputes Redressal Commission \n Esha Sajgotra vs <b>Mvd</b> University on 10 February, 2011    \n \n \n \n \n \n  \n \n \n \n \n \n\n \n \n\n\n\n\n\n\n\n \n\n\n\n \n\n J",
        "docsize": 36646,
        "tid": 129413518,
        "covertids": [],
        "doctype": 186,
        "publishdate": "2011-02-10",
        "firstname": None,
        "secondname": None,
        "lastname": None,
        "fragment": True,
        "docsource": "State Consumer Disputes Redressal Commission",
        "covers": []
      },
      {
        "title": "Mohd. Umar vs Union Of India And Others on 29 July, 2013",
        "covertitles": [],
        "numcites": 1,
        "numcitedby": 0,
        "url": None,
        "headline": " Central Administrative Tribunal - Allahabad \n Mohd. Umar vs Union Of India And Others on 29 July",
        "docsize": 20739,
        "tid": 142103944,
        "covertids": [],
        "doctype": 103,
        "publishdate": "2013-07-29",
        "firstname": None,
        "secondname": None,
        "lastname": None,
        "fragment": True,
        "docsource": "Central Administrative Tribunal - Allahabad",
        "covers": []
      }
    ],
    "found": "51 - 60 of 71",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [
      {
        "title": "Shri Rajeshwar Nath & Ors. vs . M/S. Diwan Chand Builders (P) ... on 30 March, 2007",
        "covertitles": [],
        "numcites": 0,
        "numcitedby": 0,
        "url": None,
        "headline": " Delhi District Court \n Shri Rajeshwar Nath &amp; Ors. vs . M/S. Diwan Chand Builders (P",
        "docsize": 162690,
        "tid": 179654621,
        "covertids": [],
        "doctype": 1100,
        "publishdate": "2007-03-30",
        "firstname": "s",
        "secondname": "i",
        "lastname": "singh",
        "fragment": True,
        "docsource": "Delhi District Court",
        "author": "S I Singh",
        "authorEncoded": "S%20I%20Singh",
        "covers": []
      }
    ],
    "found": "71 - 71 of 71",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "companies act 1956",
            "formInput": "companies%20act%201956"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "delhi",
            "formInput": "MVD%20Act+doctypes:delhi",
            "selected": False
          },
          {
            "value": "punjab",
            "formInput": "MVD%20Act+doctypes:punjab",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "R Easwar",
            "formInput": "MVD%20Act+author:R Easwar"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2016,
            "formInput": "MVD%20Act+fromdate:1-1-2016+todate:31-12-2016"
          }
        ]
      ]
    ],
    "docs": [
      {
        "title": "United India Insurance Co. Ltd. vs Lilabai And Ors. on 9 September, 2005",
        "covertitles": [],
        "numcites": 4,
        "numcitedby": 0,
        "url": None,
        "headline": "meaning of Section 2(5- A) of Motor Vehicles <b>Act</b> , 1939. Thirdly, the learned Member was wrong in holding that ... relationship is not in dispute.\n  \n\n (ii) The scooter (No. <b>MVD</b> 6455) was owned by Ramesh Patil, respondent",
        "docsize": 10145,
        "tid": 1704045,
        "covertids": [],
        "doctype": 22,
        "publishdate": "2005-09-09",
        "firstname": "v",
        "secondname": None,
        "lastname": "munshi",
        "fragment": True,
        "docsource": "Bombay High Court",
        "author": "V Munshi",
        "authorEncoded": "V%20Munshi",
        "citation": "2007 ACJ 1534",
        "covers": []
      },
      {
        "title": "M.N. Pushpavalli vs State Of Karnataka on 20 August, 1984",
        "covertitles": [],
        "numcites": 1,
        "numcitedby": 0,
        "url": None,
        "headline": "Karnataka Stamp <b>Act</b>, 1957 (Karnataka <b>Act</b> 34 of 1957) (hereinafter referred to as the <b>Act</b>) was paid which also ... concerned Registering Officer under the Indian Registration <b>Act</b> of 1908.\n  \n\n 3. On a reference made by the Registering Officer",
        "docsize": 12264,
        "tid": 289650,
        "covertids": [],
        "doctype": 37,
        "publishdate": "1984-08-20",
        "firstname": None,
        "secondname": None,
        "lastname": "puttaswamy",
        "fragment": True,
        "docsource": "Karnataka High Court",
        "author": "Puttaswamy",
        "authorEncoded": "Puttaswamy",
        "citation": "ILR 1985 KAR 3733",
        "covers": []
      },
      {
        "title": "M/S Sumangala Properties vs The District Registrar Cum on 27 August, 2014",
        "covertitles": [],
        "numcites": 1,
        "numcitedby": 0,
        "url": "http://judgmenthck.kar.nic.in/judgmentsdsp/bitstream/123456789/14923/1/WP273-13-27-08-2014.pdf",
        "headline": "TREE HOTELS PVT. LTD.,\n        (COMPANY INCORPORATED UNDER THE\n        COMPANIES <b>ACT</b>, 1956)\n        REP. BY ITS MANAGING DIRECTOR\n        HAVING ITS REGISTERED OFFICE ... YADALAM BROTHERS PVT. LTD.,\n       (COMPANY INCORPORATED UNDER THE\n       COMPANIES <b>ACT</b>, 1956)\n       REP. BY ITS MANAGING DIRECTOR\n       HAVING ITS REGISTERED OFFICE",
        "docsize": 6050,
        "tid": 79821814,
        "covertids": [],
        "doctype": 37,
        "publishdate": "2014-08-27",
        "firstname": "a",
        "secondname": None,
        "lastname": "gowda",
        "fragment": True,
        "docsource": "Karnataka High Court",
        "author": "A Gowda",
        "authorEncoded": "A%20Gowda",
        "covers": []
      },
      {
        "title": "Nishat Roadways And Ors. vs State Of J. And K. And Ors. on 5 May, 2005",
        "covertitles": [],
        "numcites": 2,
        "numcitedby": 0,
        "url": None,
        "headline": "State Government, issued a Notification No. 4/<b>MVD</b> of 1987 dated 11-6-1987 wherein the freight rates have been ... arbitration in terms of  Section 20  of the Arbitration <b>Act</b> (hereinafter called as \"the <b>Act</b>\"). Mr. M.S. Bhat, District",
        "docsize": 7317,
        "tid": 1271722,
        "covertids": [],
        "doctype": 29,
        "publishdate": "2005-05-05",
        "firstname": "n",
        "secondname": None,
        "lastname": "singh",
        "fragment": True,
        "docsource": "Jammu & Kashmir High Court",
        "author": "N Singh",
        "authorEncoded": "N%20Singh",
        "citation": "AIR 2006 J K 21",
        "covers": []
      },
      {
        "title": "High Court Of Jammu And Kashmir At ... vs New India Assurance Co. Ltd. & Ors on 12 November, 2013",
        "covertitles": [],
        "numcites": 1,
        "numcitedby": 0,
        "url": "http://judis.nic.in/Judis_Jammu/qrydispfree.aspx?filename=1539",
        "headline": "Section 17 of the J&amp;K Consumer Protection <b>Act</b> 1987 is \ndirected against the short order dated 11.10.2011\npassed ... District Rajouri had been\nrenewed vide renewal No. 8820/<b>MVD</b>/RTOJ w.e.f  \n18.09.2004 to 17.09.2007. Even otherwise",
        "docsize": 3031,
        "tid": 147983627,
        "covertids": [],
        "doctype": 29,
        "publishdate": "2013-11-12",
        "firstname": None,
        "secondname": None,
        "lastname": None,
        "fragment": True,
        "docsource": "Jammu & Kashmir High Court",
        "covers": []
      },
      {
        "title": "Enhira Software (Exports) Ltd. ... vs State Of Maharashtra And Anr on 9 July, 2019",
        "covertitles": [],
        "numcites": 1,
        "numcitedby": 0,
        "url": "https://bombayhighcourt.nic.in/generatenewauth.php?auth=cGF0aD0uL2RhdGEvb3JpZ2luYWwvMjAxOS8mZm5hbWU9V1AyOTg4MTgwOTA3MTkucGRmJnNtZmxhZz1OJnJqdWRkYXRlPSZ1cGxvYWRkdD0wOS8wNy8yMDE5JnNwYXNzcGhyYXNlPTEwMDcxOTA0MDc0MQ==",
        "headline": "process, if a Bidder indulges in any such\n           deliberate <b>act</b> as would jeopardize or unnecessarily\n           delay the process ... under \"Terms and Conditions\".\n \n            The decision of the <b>MVD</b> regarding forfeiture of the EMD\n           and rejection of bid shall",
        "docsize": 29068,
        "tid": 70383639,
        "covertids": [],
        "doctype": 22,
        "publishdate": "2019-07-09",
        "firstname": None,
        "secondname": None,
        "lastname": None,
        "fragment": True,
        "docsource": "Bombay High Court",
        "covers": []
      },
      {
        "title": "P.A.Janish vs State Of Kerala on 1 September, 2021",
        "covertitles": [],
        "numcites": 12,
        "numcitedby": 0,
        "url": "https://hckinfo.kerala.gov.in/digicourt/orders/interimorder/2021/215700170912021_3.pdf",
        "headline": "direction interdicting the officers of the Motor Vehicles\nDepartment (<b>MVD</b>) under the 3rd respondent from wearing &#x27;blue beret caps ... Police Officers under Section 43\nof the Kerala Police <b>Act</b>, 2011, pending disposal of the writ petition.\n\n      This petition again",
        "docsize": 23368,
        "tid": 137132251,
        "covertids": [],
        "doctype": 30,
        "publishdate": "2021-09-01",
        "firstname": None,
        "secondname": None,
        "lastname": None,
        "fragment": True,
        "docsource": "Kerala High Court",
        "covers": []
      },
      {
        "title": "New India Assurance Co. Ltd vs Mohd Ishfaq And Others on 27 July, 2020",
        "covertitles": [],
        "numcites": 2,
        "numcitedby": 0,
        "url": "https://services.ecourts.gov.in/ecourtindiaHC/cases/display_pdf.php?filename=oo%2BtRJJeFk03ErxBsOJjIDefexv1d9pjmwbXgv%2BxckDMWwbImZ3t26HNUJbaOFkj&caseno=MA%2F429%2F2010&cCode=1&appFlag=",
        "headline": "claimant as loss of earning capacity and,\n\ntherefore, <b>acted</b> in derogation of the law laid down by the Supreme Court ... brought the record of\n\nlicence No.4622/<b>MVD</b>/R date d 23.08.03 issued by the ARTO Rajouri in\n\nfavour",
        "docsize": 8677,
        "tid": 33911781,
        "covertids": [],
        "doctype": 29,
        "publishdate": "2020-07-27",
        "firstname": None,
        "secondname": None,
        "lastname": None,
        "fragment": True,
        "docsource": "Jammu & Kashmir High Court",
        "covers": []
      },
      {
        "title": "B Chikka Hanumaiah vs The Divisional Commissioner on 25 October, 2018",
        "covertitles": [],
        "numcites": 1,
        "numcitedby": 0,
        "url": "http://judgmenthck.kar.nic.in/judgmentsdsp/bitstream/123456789/238113/1/WP35076-12-25-10-2018.pdf",
        "headline": "CONFIRMING THE IMPUGNED ORDER DATED\n25.10.2003 IN CASE NO.<b>MVD</b>/Y/757/1993-94\nPASSED BY THE RESPONDENT ... Division,     whereby   the\n\norder         dated       25.10.2003         in    case      No.<b>MVD</b>/Y/\n\n757/1993-94               passed     by     the    Deputy      Inspector\n\nGeneral",
        "docsize": 7728,
        "tid": 114144233,
        "covertids": [],
        "doctype": 37,
        "publishdate": "2018-10-25",
        "firstname": "r",
        "secondname": None,
        "lastname": "devdas",
        "fragment": True,
        "docsource": "Karnataka High Court",
        "author": "R Devdas",
        "authorEncoded": "R%20Devdas",
        "covers": []
      },
      {
        "title": "Balwan Singh vs M/S Bajaj Allianz General ... on 21 May, 2019",
        "covertitles": [],
        "numcites": 3,
        "numcitedby": 0,
        "url": None,
        "headline": "Section 149\n\n(2) of the  Motor Vehicles <b>Act</b> , 1988 (in short, 'the <b>Act</b>').\n\n               Counsel for the insurance company ... perusal thereof would reveal that licence bearing No.\n\n8183/<b>MVD</b>/RTOJ was originally issued by Regional Transport Officer,\n\nJammu",
        "docsize": 9202,
        "tid": 164348984,
        "covertids": [],
        "doctype": 40,
        "publishdate": "2019-05-21",
        "firstname": None,
        "secondname": None,
        "lastname": None,
        "fragment": True,
        "docsource": "Punjab-Haryana High Court",
        "covers": []
      }
    ],
    "found": "11 - 20 of 71",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "companies act 1956",
            "formInput": "companies%20act%201956"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "delhi",
            "formInput": "MVD%20Act+doctypes:delhi",
            "selected": False
          },
          {
            "value": "punjab",
            "formInput": "MVD%20Act+doctypes:punjab",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "R Easwar",
            "formInput": "MVD%20Act+author:R Easwar"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2016,
            "formInput": "MVD%20Act+fromdate:1-1-2016+todate:31-12-2016"
          }
        ]
      ]
    ],
    "docs": [
      {
        "title": "Vide This Order I Shall Dispose Of ... vs Unknown on 29 February, 2016",
        "covertitles": [],
        "numcites": 5,
        "numcitedby": 0,
        "url": "http://judis.nic.in/DDC/list_new2.asp?Jud_Pdf_Name=tt1123800009010290216.pdf&JudYear=2016",
        "headline": "read with\n Section 13  (1) (d) of  PC <b>Act</b> , titled as CBI vs. Vipul Sharma\netc., has no relevance with ... <b>MVD</b> Infotech Pvt. Ltd. vs. Vipul Sharma        2/3\n   7.              On the basis of above observation and discussion,\napplication",
        "docsize": 4384,
        "tid": 60490430,
        "covertids": [],
        "doctype": 1100,
        "publishdate": "2016-02-29",
        "firstname": "s",
        "secondname": None,
        "lastname": "kumar",
        "fragment": True,
        "docsource": "Delhi District Court",
        "author": "S Kumar",
        "authorEncoded": "S%20Kumar",
        "covers": []
      },
      {
        "title": "M/S. Sasken Communication ... vs The Joint Commissioner Of ... on 15 April, 2011",
        "covertitles": [],
        "numcites": 6,
        "numcitedby": 1,
        "url": "http://judgmenthck.kar.nic.in/judgments/bitstream/123456789/591616/1/WA90-11-15-04-2011.pdf",
        "headline": " Karnataka High Court \n M/S. Sasken Communication ... vs The Joint Commissioner Of ... on 15 April",
        "docsize": 127097,
        "tid": 21069700,
        "covertids": [],
        "doctype": 37,
        "publishdate": "2011-04-15",
        "firstname": "n",
        "secondname": "a",
        "lastname": "malimath",
        "fragment": True,
        "docsource": "Karnataka High Court",
        "author": "N A Malimath",
        "authorEncoded": "N%20A%20Malimath",
        "covers": []
      },
      {
        "title": "National Insurance Co Ltd vs Unknown on 13 October, 2009",
        "covertitles": [],
        "numcites": 3,
        "numcitedby": 0,
        "url": "http://judis.nic.in/Judis_Jammu/qrydispfree.aspx?filename=452",
        "headline": " Jammu & Kashmir High Court \n National Insurance Co Ltd vs Unknown on 13 October, 2009         \n\n  \n\n  \n\n \n\n \n \n HIGH",
        "docsize": 35118,
        "tid": 1775463,
        "covertids": [],
        "doctype": 29,
        "publishdate": "2009-10-13",
        "firstname": None,
        "secondname": None,
        "lastname": None,
        "fragment": True,
        "docsource": "Jammu & Kashmir High Court",
        "covers": []
      },
      {
        "title": "Romesh Kr. Samotra And Ors. vs State Of J And K And Ors. on 22 September, 2004",
        "covertitles": [],
        "numcites": 2,
        "numcitedby": 0,
        "url": None,
        "headline": " Jammu & Kashmir High Court \n Romesh Kr. Samotra And Ors. vs State Of J And K",
        "docsize": 39914,
        "tid": 1607468,
        "covertids": [],
        "doctype": 29,
        "publishdate": "2004-09-22",
        "firstname": "v",
        "secondname": None,
        "lastname": "jhanji",
        "fragment": True,
        "docsource": "Jammu & Kashmir High Court",
        "author": "V Jhanji",
        "authorEncoded": "V%20Jhanji",
        "citation": "2004 (3) JKJ 258",
        "covers": []
      },
      {
        "title": "Jewellery Pvt. Ltd vs Dham on 7 February, 2014",
        "covertitles": [],
        "numcites": 5,
        "numcitedby": 0,
        "url": "http://bombayhighcourt.nic.in/generatenewauth.php?auth=cGF0aD0uL2RhdGEvanVkZ2VtZW50cy8yMDE0LyZmbmFtZT1PU0NQNDk4MTEucGRmJnNtZmxhZz1O",
        "headline": " Bombay High Court \n Jewellery Pvt. Ltd vs Dham on 7 February, 2014  Bench: G.S",
        "docsize": 35948,
        "tid": 130371985,
        "covertids": [],
        "doctype": 22,
        "publishdate": "2014-02-07",
        "firstname": None,
        "secondname": None,
        "lastname": None,
        "fragment": True,
        "docsource": "Bombay High Court",
        "covers": []
      },
      {
        "title": "Jewellery Pvt. Ltd vs Dham on 7 February, 2014",
        "covertitles": [],
        "numcites": 5,
        "numcitedby": 0,
        "url": "http://bombayhighcourt.nic.in/generatenewauth.php?auth=cGF0aD0uL2RhdGEvanVkZ2VtZW50cy8yMDE0LyZmbmFtZT1PU0NBNDE3MTIucGRmJnNtZmxhZz1O",
        "headline": " Bombay High Court \n Jewellery Pvt. Ltd vs Dham on 7 February, 2014  Bench: G.S",
        "docsize": 35948,
        "tid": 139490592,
        "covertids": [],
        "doctype": 22,
        "publishdate": "2014-02-07",
        "firstname": None,
        "secondname": None,
        "lastname": None,
        "fragment": True,
        "docsource": "Bombay High Court",
        "covers": []
      },
      {
        "title": "Dinesha vs State By Shikaripura Police on 24 September, 2010",
        "covertitles": [],
        "numcites": 4,
        "numcitedby": 0,
        "url": "http://judgmenthck.kar.nic.in/judgments/bitstream/123456789/463474/2/CRLA1330-06-24-09-2010.pdf",
        "headline": " Karnataka High Court \n Dinesha vs State By Shikaripura Police on 24 September, 2010  Author: V",
        "docsize": 39979,
        "tid": 604270,
        "covertids": [],
        "doctype": 37,
        "publishdate": "2010-09-24",
        "firstname": "v",
        "secondname": "a",
        "lastname": "k.govindarajulu",
        "fragment": True,
        "docsource": "Karnataka High Court",
        "author": "V A K.Govindarajulu",
        "authorEncoded": "V%20A%20K.Govindarajulu",
        "covers": []
      },
      {
        "title": "Santosh Kumar Bhowmik And Anr. vs O.N.G.C. And Anr. on 28 September, 1999",
        "covertitles": [],
        "numcites": 5,
        "numcitedby": 0,
        "url": None,
        "headline": " Gauhati High Court \n Santosh Kumar Bhowmik And Anr. vs O.N.G.C. And Anr",
        "docsize": 21302,
        "tid": 1821384,
        "covertids": [],
        "doctype": 28,
        "publishdate": "1999-09-28",
        "firstname": "p",
        "secondname": None,
        "lastname": "phukan",
        "fragment": True,
        "docsource": "Gauhati High Court",
        "author": "P Phukan",
        "authorEncoded": "P%20Phukan",
        "citation": "(2000) IILLJ 161 Gau",
        "covers": []
      },
      {
        "title": "Sri.Puttamadegowda vs Sri.Basavaraju on 7 January, 2011",
        "covertitles": [],
        "numcites": 6,
        "numcitedby": 0,
        "url": "http://judgmenthck.kar.nic.in/judgments/bitstream/123456789/509737/1/RSA763-09-07-01-2011.pdf",
        "headline": " Karnataka High Court \n Sri.Puttamadegowda vs Sri.Basavaraju on 7 January, 2011  Author: L.Narayana",
        "docsize": 14536,
        "tid": 134405741,
        "covertids": [],
        "doctype": 37,
        "publishdate": "2011-01-07",
        "firstname": "l",
        "secondname": None,
        "lastname": "swamy",
        "fragment": True,
        "docsource": "Karnataka High Court",
        "author": "L Swamy",
        "authorEncoded": "L%20Swamy",
        "covers": []
      },
      {
        "title": "Dineshchandra Viththalbhai ... vs By This Writ Application In The ... on 5 September, 2014",
        "covertitles": [],
        "numcites": 1,
        "numcitedby": 0,
        "url": None,
        "headline": " Gujarat High Court \n Dineshchandra Viththalbhai ... vs By This Writ Application In The ... on 5 September",
        "docsize": 41685,
        "tid": 23439452,
        "covertids": [],
        "doctype": 34,
        "publishdate": "2014-09-05",
        "firstname": None,
        "secondname": None,
        "lastname": None,
        "fragment": True,
        "docsource": "Gujarat High Court",
        "covers": []
      }
    ],
    "found": "31 - 40 of 71",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [
      {
        "title": "R Srinivasan vs K. Vaidyanath on 17 October, 2020",
        "covertitles": [],
        "numcites": 18,
        "numcitedby": 0,
        "url": "https://services.ecourts.gov.in/ecourtindia_v4_bilingual/cases/display_pdf.php?filename=%2Forders%2F2018%2F201700252482018_1.pdf&caseno=CRL.A%2F25248%2F2018&cCode=7&appFlag=web&normal_v=1",
        "headline": " Bangalore District Court \n R Srinivasan vs K. Vaidyanath on 17 October, 2020  IN THE COURT",
        "docsize": 79292,
        "tid": 192340127,
        "covertids": [],
        "doctype": 1101,
        "publishdate": "2020-10-17",
        "firstname": None,
        "secondname": None,
        "lastname": None,
        "fragment": True,
        "docsource": "Bangalore District Court",
        "covers": []
      },
      {
        "title": "The Ito(Inte.Taxa)-1, Ahmedabad vs Madhav Vasant Dalvi, Ahmedabad on 27 July, 2022",
        "covertitles": [],
        "numcites": 10,
        "numcitedby": 0,
        "url": "https://www.itat.gov.in/files/uploads/categoryImage/1658914998-ITA%20No.%20995-Ahd-2019.pdf",
        "headline": " Income Tax Appellate Tribunal - Ahmedabad \n The Ito(Inte.Taxa)-1, Ahmedabad vs Madhav Vasant Dalvi",
        "docsize": 21458,
        "tid": 193199050,
        "covertids": [],
        "doctype": 142,
        "publishdate": "2022-07-27",
        "firstname": None,
        "secondname": None,
        "lastname": None,
        "fragment": True,
        "docsource": "Income Tax Appellate Tribunal - Ahmedabad",
        "covers": []
      },
      {
        "title": "<b>Mvd</b> Satyanaryana vs South Eastern Railway (Kolkata) on 26 March, 2021",
        "covertitles": [],
        "numcites": 1,
        "numcitedby": 0,
        "url": "https://dsscic.nic.in/cause-list-report-web/download",
        "headline": " Central Information Commission \n <b>Mvd</b> Satyanaryana vs South Eastern Railway (Kolkata) on 26 March, 2021  Author",
        "docsize": 20812,
        "tid": 145037232,
        "covertids": [],
        "doctype": 131,
        "publishdate": "2021-03-26",
        "firstname": "a",
        "secondname": None,
        "lastname": "pandove",
        "fragment": True,
        "docsource": "Central Information Commission",
        "author": "A Pandove",
        "authorEncoded": "A%20Pandove",
        "covers": []
      },
      {
        "title": "Mr.Shivalal vs Mr. John Kennedy on 1 September, 2021",
        "covertitles": [],
        "numcites": 1,
        "numcitedby": 0,
        "url": "https://services.ecourts.gov.in/ecourtindia_v4_bilingual/cases/display_pdf.php?filename=%2Forders%2F2016%2F205200258282016_6.pdf&caseno=O.S.%2F25828%2F2016&cCode=7&appFlag=web&normal_v=1",
        "headline": " Bangalore District Court \n Mr.Shivalal vs Mr. John Kennedy on 1 September, 2021     IN THE",
        "docsize": 28584,
        "tid": 45883663,
        "covertids": [],
        "doctype": 1101,
        "publishdate": "2021-09-01",
        "firstname": None,
        "secondname": None,
        "lastname": None,
        "fragment": True,
        "docsource": "Bangalore District Court",
        "covers": []
      },
      {
        "title": "<b>Mvd</b> Satyanaryana vs South Eastern Railway (Kolkata) on 30 July, 2020",
        "covertitles": [],
        "numcites": 1,
        "numcitedby": 0,
        "url": "https://dsscic.nic.in/cause-list-report-web/download",
        "headline": " Central Information Commission \n <b>Mvd</b> Satyanaryana vs South Eastern Railway (Kolkata) on 30 July, 2020  Author",
        "docsize": 13006,
        "tid": 158122112,
        "covertids": [],
        "doctype": 131,
        "publishdate": "2020-07-30",
        "firstname": "a",
        "secondname": None,
        "lastname": "pandove",
        "fragment": True,
        "docsource": "Central Information Commission",
        "author": "A Pandove",
        "authorEncoded": "A%20Pandove",
        "covers": []
      },
      {
        "title": "Vinod Sharma vs . Vipul Sharma Cc No. 5454/11 1 Of 17 on 22 September, 2014",
        "covertitles": [],
        "numcites": 17,
        "numcitedby": 0,
        "url": None,
        "headline": " Delhi District Court \n Vinod Sharma vs . Vipul Sharma Cc No. 5454/11 1 Of 17",
        "docsize": 45724,
        "tid": 149558654,
        "covertids": [],
        "doctype": 1100,
        "publishdate": "2014-09-22",
        "firstname": "s",
        "secondname": "b",
        "lastname": "chugh",
        "fragment": True,
        "docsource": "Delhi District Court",
        "author": "S B Chugh",
        "authorEncoded": "S%20B%20Chugh",
        "covers": []
      },
      {
        "title": ") Smt. Rojan Vivi vs ) Manoj Kumar on 19 April, 2012",
        "covertitles": [],
        "numcites": 10,
        "numcitedby": 0,
        "url": None,
        "headline": " Delhi District Court \n ) Smt. Rojan Vivi vs ) Manoj Kumar on 19 April, 2012  Author: Sh",
        "docsize": 26591,
        "tid": 99427924,
        "covertids": [],
        "doctype": 1100,
        "publishdate": "2012-04-19",
        "firstname": "s",
        "secondname": "d",
        "lastname": "malhotra",
        "fragment": True,
        "docsource": "Delhi District Court",
        "author": "S D Malhotra",
        "authorEncoded": "S%20D%20Malhotra",
        "covers": []
      },
      {
        "title": "Smt. Usha Rani vs Smt. Kanta on 26 February, 2011",
        "covertitles": [],
        "numcites": 5,
        "numcitedby": 0,
        "url": None,
        "headline": " Delhi District Court \n Smt. Usha Rani vs Smt. Kanta on 26 February, 2011  Author: Sh",
        "docsize": 20721,
        "tid": 16924350,
        "covertids": [],
        "doctype": 1100,
        "publishdate": "2011-02-26",
        "firstname": "s",
        "secondname": "g",
        "lastname": "jindal",
        "fragment": True,
        "docsource": "Delhi District Court",
        "author": "S G Jindal",
        "authorEncoded": "S%20G%20Jindal",
        "covers": []
      },
      {
        "title": "Smt. Usha vs Smt. Kanta on 17 February, 2012",
        "covertitles": [],
        "numcites": 4,
        "numcitedby": 0,
        "url": None,
        "headline": " Delhi District Court \n Smt. Usha vs Smt. Kanta on 17 February, 2012  Author: Sh. Sanjeev",
        "docsize": 27446,
        "tid": 192634493,
        "covertids": [],
        "doctype": 1100,
        "publishdate": "2012-02-17",
        "firstname": "s",
        "secondname": "s",
        "lastname": "aggarwal",
        "fragment": True,
        "docsource": "Delhi District Court",
        "author": "S S Aggarwal",
        "authorEncoded": "S%20S%20Aggarwal",
        "covers": []
      },
      {
        "title": "Smt. Krishna Kali vs Ram Surat Received Fatal Injuries ... on 30 March, 2007",
        "covertitles": [],
        "numcites": 6,
        "numcitedby": 0,
        "url": None,
        "headline": "seek  verification of  D/L No. 670/<b>MVD</b>/03/D stated to have\n\n  been issued by Licensing Authority (MV Department ... defence under section 149(2) of the M. V.\n\n  <b>Act</b> has been exhaustively discussed by the Apex Court",
        "docsize": 20939,
        "tid": 37261295,
        "covertids": [],
        "doctype": 1100,
        "publishdate": "2007-03-30",
        "firstname": "s",
        "secondname": "s",
        "lastname": "garg",
        "fragment": True,
        "docsource": "Delhi District Court",
        "author": "S S Garg",
        "authorEncoded": "S%20S%20Garg",
        "covers": []
      }
    ],
    "found": "61 - 70 of 71",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "companies act 1956",
            "formInput": "companies%20act%201956"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "delhi",
            "formInput": "MVD%20Act+doctypes:delhi",
            "selected": False
          },
          {
            "value": "punjab",
            "formInput": "MVD%20Act+doctypes:punjab",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "R Easwar",
            "formInput": "MVD%20Act+author:R Easwar"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2016,
            "formInput": "MVD%20Act+fromdate:1-1-2016+todate:31-12-2016"
          }
        ]
      ]
    ],
    "docs": [
      {
        "title": "Sri. Ramanjaneya vs State Of Karnataka on 5 May, 2011",
        "covertitles": [],
        "numcites": 2,
        "numcitedby": 0,
        "url": "http://judgmenthck.kar.nic.in/judgments/bitstream/123456789/535697/1/CRLP2256-11-05-05-2011.pdf",
        "headline": " Karnataka High Court \n Sri. Ramanjaneya vs State Of Karnataka on 5 May, 2011  Author: K",
        "docsize": 36539,
        "tid": 179618239,
        "covertids": [],
        "doctype": 37,
        "publishdate": "2011-05-05",
        "firstname": None,
        "secondname": None,
        "lastname": "k.n.keshavanarayana",
        "fragment": True,
        "docsource": "Karnataka High Court",
        "author": "K.N.Keshavanarayana",
        "authorEncoded": "K.N.Keshavanarayana",
        "covers": []
      },
      {
        "title": "Y C Anjaneya Reddy @ Y C Anjaneya vs M S Syws Madar S/O Syed Sabi on 22 January, 2010",
        "covertitles": [],
        "numcites": 1,
        "numcitedby": 0,
        "url": "http://judgmenthck.kar.nic.in/judgments/bitstream/123456789/275031/1/MFA4944-04-22-01-2010.pdf",
        "headline": "4944/2004 {<b>MVD</b>\n\nY C A11jar1Veyei'*E1ed't:i;g  \"\n \n @ YC :AI1janéy'?;_.. M   \nS/0 1&amp;1f.€t_ Ch0wda ... ur1de'1\",sc'jtVi0h .173'-(V_iv}__ bf  MV <b>Act</b>  against\nthe judgment",
        "docsize": 6896,
        "tid": 915262,
        "covertids": [],
        "doctype": 37,
        "publishdate": "2010-01-22",
        "firstname": "m",
        "secondname": "c",
        "lastname": "gowda",
        "fragment": True,
        "docsource": "Karnataka High Court",
        "author": "M C Gowda",
        "authorEncoded": "M%20C%20Gowda",
        "covers": []
      },
      {
        "title": "D V Jegarakal vs State Of Karnataka on 5 June, 2008",
        "covertitles": [],
        "numcites": 2,
        "numcitedby": 0,
        "url": "http://judgmenthck.kar.nic.in/judgments/bitstream/123456789/21243/1/CRLP4962-06%2005-06-2008.pdf",
        "headline": " Karnataka High Court \n D V Jegarakal vs State Of Karnataka on 5 June, 2008  Author",
        "docsize": 6812,
        "tid": 226309,
        "covertids": [],
        "doctype": 37,
        "publishdate": "2008-06-05",
        "firstname": "h",
        "secondname": "n",
        "lastname": "das",
        "fragment": True,
        "docsource": "Karnataka High Court",
        "author": "H N Das",
        "authorEncoded": "H%20N%20Das",
        "covers": []
      },
      {
        "title": "Sri Chekkera B Bharath S/O Lae ... vs Smt Suman Nanaiah W/O C B Bharath on 16 June, 2011",
        "covertitles": [],
        "numcites": 1,
        "numcitedby": 0,
        "url": "http://judgmenthck.kar.nic.in/judgments/bitstream/123456789/550717/1/MFA631-07-16-06-2011.pdf",
        "headline": "HONBLE MR. JUSTICE4N.E{;i5;§*'I€E.L4   \n\n<b>MVD</b>\n\nTHE HONBLE ... petitien filed under Seetien 13.1,\n\n. (Ea) of Hindu Marriage <b>Act</b> fer disselution Qf marriage by a\n\ndecree of diverse,\n\nThis",
        "docsize": 1996,
        "tid": 138193122,
        "covertids": [],
        "doctype": 37,
        "publishdate": "2011-06-16",
        "firstname": "n",
        "secondname": "a",
        "lastname": "nagaraj",
        "fragment": True,
        "docsource": "Karnataka High Court",
        "author": "N A Nagaraj",
        "authorEncoded": "N%20A%20Nagaraj",
        "covers": []
      },
      {
        "title": "Abdul Raheem vs The District Collector on 13 January, 2020",
        "covertitles": [],
        "numcites": 1,
        "numcitedby": 0,
        "url": "https://services.ecourts.gov.in/ecourtindiaHC/cases/display_pdf.php?filename=%2FE3WiyNUWFIaR1oBGE62Wi5b%2FZd%2BUPVSYo7FjDHkBgqM53LpgBJ2Os0J3Ko%2B8x22&caseno=WP%28C%29%2F33335%2F2019&cCode=1&appFlag=",
        "headline": " Kerala High Court \n Abdul Raheem vs The District Collector on 13 January, 2020                 IN THE",
        "docsize": 17684,
        "tid": 156105551,
        "covertids": [],
        "doctype": 30,
        "publishdate": "2020-01-13",
        "firstname": None,
        "secondname": None,
        "lastname": None,
        "fragment": True,
        "docsource": "Kerala High Court",
        "covers": []
      },
      {
        "title": "M/S Sumo Taxi Stand And Anr vs State Of Jk And Ors on 24 February, 2021",
        "covertitles": [],
        "numcites": 4,
        "numcitedby": 0,
        "url": "https://services.ecourts.gov.in/ecourtindiaHC/cases/display_pdf.php?filename=%2FE3WiyNUWFIaR1oBGE62Wue%2FMLqtSF1l5CYWBkfvuRPMbX6zSbfAHOX1e%2BkGF%2BK%2B&caseno=WP%28C%29%2F2821%2F2019&cCode=2&appFlag=",
        "headline": " Jammu & Kashmir High Court - Srinagar Bench \n M/S Sumo Taxi Stand And Anr vs State",
        "docsize": 17506,
        "tid": 56742968,
        "covertids": [],
        "doctype": 46,
        "publishdate": "2021-02-24",
        "firstname": None,
        "secondname": None,
        "lastname": None,
        "fragment": True,
        "docsource": "Jammu & Kashmir High Court - Srinagar Bench",
        "covers": []
      },
      {
        "title": "State Of J&K; vs Rajeev Kumar on 28 December, 2018",
        "covertitles": [],
        "numcites": 8,
        "numcitedby": 0,
        "url": "http://lobis.nic.in/ddir/jk/SKG/judgement/28-12-2018/SKG28122018CRAA422005.pdf",
        "headline": "spot.   Application    form     learning    licence    form\n     No.9385/LA/<b>MVD</b>/98 age proof certificate, medical form\n     along with two photographs ... investigation\n     offences under  Section 5(2)  P.C. <b>Act</b>, 2006 r/w 161 RPC\n     were prima facie made out against",
        "docsize": 27550,
        "tid": 127685152,
        "covertids": [],
        "doctype": 29,
        "publishdate": "2018-12-28",
        "firstname": None,
        "secondname": None,
        "lastname": None,
        "fragment": True,
        "docsource": "Jammu & Kashmir High Court",
        "covers": []
      },
      {
        "title": "Royal Sundaram Alliance ... vs Raja on 2 February, 2015",
        "covertitles": [],
        "numcites": 1,
        "numcitedby": 0,
        "url": "https://www.mhc.tn.gov.in/judis/index.php/casestatus/viewpdf/590177",
        "headline": " Madras High Court \n Royal Sundaram Alliance ... vs Raja on 2 February, 2015                                                                      CMA.No.1579",
        "docsize": 24472,
        "tid": 57190803,
        "covertids": [],
        "doctype": 24,
        "publishdate": "2015-02-02",
        "firstname": None,
        "secondname": None,
        "lastname": None,
        "fragment": True,
        "docsource": "Madras High Court",
        "covers": []
      },
      {
        "title": "The Chairman vs Kamalarani on 17 January, 2011",
        "covertitles": [],
        "numcites": 0,
        "numcitedby": 0,
        "url": "http://judgmenthck.kar.nic.in/judgments/bitstream/123456789/500975/1/MFA5443-05-17-01-2011.pdf",
        "headline": " Karnataka High Court \n The Chairman vs Kamalarani on 17 January, 2011  Author: K.L.Manjunath",
        "docsize": 28826,
        "tid": 114272328,
        "covertids": [],
        "doctype": 37,
        "publishdate": "2011-01-17",
        "firstname": "k",
        "secondname": "a",
        "lastname": "h.g.ramesh",
        "fragment": True,
        "docsource": "Karnataka High Court",
        "author": "K A H.G.Ramesh",
        "authorEncoded": "K%20A%20H.G.Ramesh",
        "covers": []
      },
      {
        "title": "United India Insurance Co. Ltd vs Charlie (2005(10) Scc 720) on 9 February, 2011",
        "covertitles": [],
        "numcites": 9,
        "numcitedby": 0,
        "url": "http://judis.nic.in/Judis_SriNagar/qrydisp.aspx?filename=1243",
        "headline": " Jammu & Kashmir High Court - Srinagar Bench \n United India Insurance Co. Ltd vs Charlie (2005(10",
        "docsize": 35252,
        "tid": 40927711,
        "covertids": [],
        "doctype": 46,
        "publishdate": "2011-02-09",
        "firstname": None,
        "secondname": None,
        "lastname": None,
        "fragment": True,
        "docsource": "Jammu & Kashmir High Court - Srinagar Bench",
        "covers": []
      }
    ],
    "found": "41 - 50 of 71",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "companies act 1956",
            "formInput": "companies%20act%201956"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "delhi",
            "formInput": "MVD%20Act+doctypes:delhi",
            "selected": False
          },
          {
            "value": "punjab",
            "formInput": "MVD%20Act+doctypes:punjab",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "R Easwar",
            "formInput": "MVD%20Act+author:R Easwar"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2016,
            "formInput": "MVD%20Act+fromdate:1-1-2016+todate:31-12-2016"
          }
        ]
      ]
    ],
    "docs": [
      {
        "title": "National Ins. Co. Ltd vs Unknown on 30 June, 2016",
        "covertitles": [],
        "numcites": 2,
        "numcitedby": 0,
        "url": "http://judis.nic.in/Judis_Jammu/list_new2.asp?FileName=2007",
        "headline": "finding of the Assistant Commissioner under Workmen\u0012s \n Compensation <b>Act</b>  is perverse inasmuch as there is no material\non record ... ARTO Udhampur who  \nstated that License No. 12368/<b>MVD</b>/J issued by Licensing \n 3 \nAuthority Jammu has been renewed",
        "docsize": 11643,
        "tid": 71311389,
        "covertids": [],
        "doctype": 29,
        "publishdate": "2016-06-30",
        "firstname": None,
        "secondname": None,
        "lastname": None,
        "fragment": True,
        "docsource": "Jammu & Kashmir High Court",
        "covers": []
      },
      {
        "title": "National Ins.Co.Ltd. vs Mohd.Missri And Ors. on 30 June, 2016",
        "covertitles": [],
        "numcites": 1,
        "numcitedby": 0,
        "url": "http://lobis.nic.in/ddir/jk/oldjud/RS30062016CIMA3112009.pdf",
        "headline": "finding of the Assistant Commissioner under Workmen's\n Compensation <b>Act</b>  is perverse inasmuch as there is no material\non record ... ARTO Udhampur who\nstated that License No. 12368/<b>MVD</b>/J issued by Licensing\n                                   3 \n\n\nAuthority Jammu has been renewed",
        "docsize": 13304,
        "tid": 14689323,
        "covertids": [],
        "doctype": 29,
        "publishdate": "2016-06-30",
        "firstname": None,
        "secondname": None,
        "lastname": None,
        "fragment": True,
        "docsource": "Jammu & Kashmir High Court",
        "covers": []
      },
      {
        "title": "Reni Mathew vs The State Of Kerala on 30 October, 2020",
        "covertitles": [],
        "numcites": 2,
        "numcitedby": 0,
        "url": "https://services.ecourts.gov.in/ecourtindiaHC/cases/display_pdf.php?filename=U%2BbhtlrLe2adAHN8Tz%2F1d%2FQqZyM%2Ff%2FDHxgfOpOAWyj9N1btXPHdXtUL8U3u1V4D3&caseno=WP%28C%29%2F23235%2F2020&cCode=1&appFlag=",
        "headline": "coercive steps,\n\ninvoking the provisions of the  Revenue Recovery <b>Act</b> , for\n\nrecovering the tax dues ... True COPY OF THE TAX DETAILS AVAILABLE\n                             IN <b>MVD</b> SITE,\n\nEXHIBIT P3                   True COPY OF THE REQUEST DATED\n                             23.10.2020.\n \n EXHIBIT",
        "docsize": 5265,
        "tid": 80263154,
        "covertids": [],
        "doctype": 30,
        "publishdate": "2020-10-30",
        "firstname": None,
        "secondname": None,
        "lastname": None,
        "fragment": True,
        "docsource": "Kerala High Court",
        "covers": []
      },
      {
        "title": "Iffco Tokio General Insurance Co. ... vs Babu Gangappa Bandekar on 17 April, 2012",
        "covertitles": [],
        "numcites": 0,
        "numcitedby": 0,
        "url": "http://judgmenthck.kar.nic.in/judgments/bitstream/123456789/765795/1/MFA23379-09-17-04-2012.PDF",
        "headline": "ALED U/S 173(1) OF MV <b>ACT</b>, 1988, AGAINST THE\nJUDGr'IF    :\\ND AWARD DATED:08/09/2009 PASSED ... award in MVCNos,69/2OO3 dated 266.2OQ9\n\nand   <b>MvD</b>,NoJ593/2OO3          dated      892OO9    on    the   file",
        "docsize": 5784,
        "tid": 24157968,
        "covertids": [],
        "doctype": 37,
        "publishdate": "2012-04-17",
        "firstname": "s",
        "secondname": None,
        "lastname": "b.adi",
        "fragment": True,
        "docsource": "Karnataka High Court",
        "author": "S B.Adi",
        "authorEncoded": "S%20B.Adi",
        "covers": []
      },
      {
        "title": "K Manjunath vs State Of Karnataka on 18 June, 2008",
        "covertitles": [],
        "numcites": 0,
        "numcitedby": 0,
        "url": "http://judgmenthck.kar.nic.in/judgments/bitstream/123456789/91687/1/CRLRP320-07%2018-06-2008.pdf",
        "headline": "Settﬁon 18d.__df\n\nEndian Mater Vehicﬁes <b>Act</b>.\n \n 3. Cage of the prosecution is that. on 2.4.2003 at abos ... mini bus in a rash and »neg§.§gen'_t <b>mvd</b>§1T:'--:V§.e;,Vés.'_:a \n\nteam: of which. the midi",
        "docsize": 5627,
        "tid": 786974,
        "covertids": [],
        "doctype": 37,
        "publishdate": "2008-06-18",
        "firstname": "s",
        "secondname": None,
        "lastname": "b.adi",
        "fragment": True,
        "docsource": "Karnataka High Court",
        "author": "S B.Adi",
        "authorEncoded": "S%20B.Adi",
        "covers": []
      },
      {
        "title": "Chain Singh vs New India Assurance Co.Ltd.And ... on 12 November, 2013",
        "covertitles": [],
        "numcites": 1,
        "numcitedby": 0,
        "url": "http://lobis.nic.in/ddir/jk/oldjud/MM12112013CIMA2852013.pdf",
        "headline": "Section 17 of the J&amp;K Consumer Protection <b>Act</b> 1987 is\n\ndirected against the short order dated 11.10.2011\n\npassed ... District Rajouri had been\n\nrenewed    vide   renewal    No.   8820/<b>MVD</b>/RTOJ        w.e.f\n\n18.09.2004 to 17.09.2007. Even otherwise",
        "docsize": 3361,
        "tid": 135964807,
        "covertids": [],
        "doctype": 29,
        "publishdate": "2013-11-12",
        "firstname": None,
        "secondname": None,
        "lastname": None,
        "fragment": True,
        "docsource": "Jammu & Kashmir High Court",
        "covers": []
      },
      {
        "title": "New India Assurance Co Ltd vs Sri S Kantaraj on 7 July, 2010",
        "covertitles": [],
        "numcites": 0,
        "numcitedby": 0,
        "url": "http://judgmenthck.kar.nic.in/judgments/bitstream/123456789/410555/1/MFA13718-07-07-07-2010.pdf",
        "headline": "IQII ;17'3(11 'OF-my  j<b>\n</b><b>ACT</b>, AGAINST TEE JUDGELENT AHD?._AWARD_  \n28.6.2006 PASSED IR live ... Insurance\nCompany  and award dated\n\n28.6.2Q('A5 vin.\"'<b>MVd</b> ﬁo.1077/2005 on the me of\n\n  ﬁmm.      rm lmcrr",
        "docsize": 1775,
        "tid": 158236857,
        "covertids": [],
        "doctype": 37,
        "publishdate": "2010-07-07",
        "firstname": "l",
        "secondname": None,
        "lastname": "swamy",
        "fragment": True,
        "docsource": "Karnataka High Court",
        "author": "L Swamy",
        "authorEncoded": "L%20Swamy",
        "covers": []
      },
      {
        "title": "Ramesh Kashyap vs Sri S M Films on 19 November, 2010",
        "covertitles": [],
        "numcites": 0,
        "numcitedby": 0,
        "url": "http://judgmenthck.kar.nic.in/judgments/bitstream/123456789/551472/1/CRLP4487-10-19-11-2010.pdf",
        "headline": "Petitioner\n\n(By Shri. Gopipraizaéfi a.iiti.ii£4XVes0ciates Advocate)\n<b>MVD</b>:  ., V ._ , \n\n f \" 'ehri ... offence puniehabie\n _ \"under Seeti0r1--i38 cf the NJ. <b>Act</b> 1881.\n\n\n\nf\\.)\n\nThis petition Gaming on for admission",
        "docsize": 1749,
        "tid": 20484060,
        "covertids": [],
        "doctype": 37,
        "publishdate": "2010-11-19",
        "firstname": "r",
        "secondname": None,
        "lastname": "malimath",
        "fragment": True,
        "docsource": "Karnataka High Court",
        "author": "R Malimath",
        "authorEncoded": "R%20Malimath",
        "covers": []
      },
      {
        "title": "M/S. Farmaz Macines Pvt. Ltd vs M/S. Graintec Industries on 13 April, 2015",
        "covertitles": [],
        "numcites": 7,
        "numcitedby": 0,
        "url": "http://services.ecourts.gov.in/ecourtindia/cases/display_pdf.php?filename=%2Forders%2F201200072752013_1.pdf&caseno=C.C.%2F7275%2F2013&cCode=2&appFlag=web",
        "headline": "OFFENCE COMPLAINED OF           :   U/Sec. 138 of  Negotiable\n                                    Instruments <b>Act</b> .\n\n\n\nPLEAD OF THE ACCUSED            :   Not guilty.\n\n\n\nFINAL ORDER                     :   Accused ... offence punishable under\n\nSection.138 of Negotiable Instruments <b>Act</b>.\n\n\n  2.   The brief facts of the complainant's case",
        "docsize": 22549,
        "tid": 145775526,
        "covertids": [],
        "doctype": 1101,
        "publishdate": "2015-04-13",
        "firstname": None,
        "secondname": None,
        "lastname": None,
        "fragment": True,
        "docsource": "Bangalore District Court",
        "covers": []
      },
      {
        "title": "M/S. Farmaz Macines Pvt. Ltd vs M/S. Graintec Industries on 13 April, 2015",
        "covertitles": [],
        "numcites": 8,
        "numcitedby": 0,
        "url": "http://services.ecourts.gov.in/ecourtindia/cases/display_pdf.php?filename=%2Forders%2F201200085142013_1.pdf&caseno=C.C.%2F8514%2F2013&cCode=2&appFlag=web",
        "headline": "OFFENCE COMPLAINED OF            :   U/Sec. 138 of  Negotiable\n                                     Instruments <b>Act</b> .\n\n\n\nPLEAD OF THE ACCUSED             :   Not guilty.\n\n\n\nFINAL ORDER                      :   Accused ... offence punishable under\n\nSection.138 of Negotiable Instruments <b>Act</b>.\n\n\n  2.   The brief facts of the complainant's case",
        "docsize": 22546,
        "tid": 60828495,
        "covertids": [],
        "doctype": 1101,
        "publishdate": "2015-04-13",
        "firstname": None,
        "secondname": None,
        "lastname": None,
        "fragment": True,
        "docsource": "Bangalore District Court",
        "covers": []
      }
    ],
    "found": "21 - 30 of 71",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  },
  {
    "categories": [
      [
        "Related Queries",
        [
          {
            "value": "driving license",
            "formInput": "driving%20license"
          },
          {
            "value": "winding up",
            "formInput": "winding%20up"
          },
          {
            "value": "sec 433",
            "formInput": "sec%20433"
          },
          {
            "value": "company petition",
            "formInput": "company%20petition"
          },
          {
            "value": "vinod sharma",
            "formInput": "vinod%20sharma"
          }
        ]
      ],
      [
        "Document Types",
        [
          {
            "value": "All",
            "formInput": "MVD%20Act",
            "selected": True
          },
          {
            "value": "Laws",
            "formInput": "MVD%20Act+doctypes:laws"
          },
          {
            "value": "Judgments",
            "formInput": "MVD%20Act+doctypes:judgments"
          },
          {
            "value": "Highcourts",
            "formInput": "MVD%20Act+doctypes:highcourts"
          },
          {
            "value": "HC & SC",
            "formInput": "MVD%20Act+doctypes:supremecourt,scorders,highcourts"
          }
        ]
      ],
      [
        "Courts",
        [
          {
            "value": "karnataka",
            "formInput": "MVD%20Act+doctypes:karnataka",
            "selected": False
          },
          {
            "value": "jammu",
            "formInput": "MVD%20Act+doctypes:jammu",
            "selected": False
          },
          {
            "value": "delhidc",
            "formInput": "MVD%20Act+doctypes:delhidc",
            "selected": False
          },
          {
            "value": "bangaloredc",
            "formInput": "MVD%20Act+doctypes:bangaloredc",
            "selected": False
          },
          {
            "value": "kerala",
            "formInput": "MVD%20Act+doctypes:kerala",
            "selected": False
          },
          {
            "value": "bombay",
            "formInput": "MVD%20Act+doctypes:bombay",
            "selected": False
          },
          {
            "value": "srinagar",
            "formInput": "MVD%20Act+doctypes:srinagar",
            "selected": False
          },
          {
            "value": "gujarat",
            "formInput": "MVD%20Act+doctypes:gujarat",
            "selected": False
          },
          {
            "value": "chennai",
            "formInput": "MVD%20Act+doctypes:chennai",
            "selected": False
          },
          {
            "value": "cic",
            "formInput": "MVD%20Act+doctypes:cic",
            "selected": False
          }
        ]
      ],
      [
        "Authors",
        [
          {
            "value": "S Kumar",
            "formInput": "MVD%20Act+author:S Kumar"
          },
          {
            "value": "J Desai",
            "formInput": "MVD%20Act+author:J Desai"
          },
          {
            "value": "S B.Adi",
            "formInput": "MVD%20Act+author:S B.Adi"
          },
          {
            "value": "L Swamy",
            "formInput": "MVD%20Act+author:L Swamy"
          },
          {
            "value": "A Pandove",
            "formInput": "MVD%20Act+author:A Pandove"
          }
        ]
      ],
      [
        "Years",
        [
          {
            "value": 2021,
            "formInput": "MVD%20Act+fromdate:1-1-2021+todate:31-12-2021"
          },
          {
            "value": 2011,
            "formInput": "MVD%20Act+fromdate:1-1-2011+todate:31-12-2011"
          },
          {
            "value": 2013,
            "formInput": "MVD%20Act+fromdate:1-1-2013+todate:31-12-2013"
          },
          {
            "value": 2010,
            "formInput": "MVD%20Act+fromdate:1-1-2010+todate:31-12-2010"
          },
          {
            "value": 2014,
            "formInput": "MVD%20Act+fromdate:1-1-2014+todate:31-12-2014"
          }
        ]
      ]
    ],
    "docs": [],
    "found": "No matching results",
    "encodedformInput": "MVD%20Act"
  }
]"""


regex = re.compile(r'''
    [\S]+:                # a key (any word followed by a colon)
    (?:
    \s                    # then a space in between
        (?!\S+:)\S+       # then a value (any word not followed by a colon)
    )+                    # match multiple values if present
    ''', re.VERBOSE)

matches = regex.findall(data)
id = []
for i in matches:
    if "tid" in i:
        dict_id = json.loads("{" + i.replace(",", "") + "}")
        try:
            id.append(dict_id['tid'])
        except:
            pass

print(len(id))