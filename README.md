# markov-text-generator

[Markov chains](https://en.wikipedia.org/wiki/Markov_chain) can be used to generate text that's (mostly) syntactically correct but often non-sensical.

This repository provides Python modules for generating markov text from any corpus you'd like.

Sample outputs
--------------

From _Emma_ by Jane Austen:
>House was taken for May and June. She was disgustingly, was suspiciously reserved. If any thing tolerable. Here was a pretty sketch of the connexion? It was an air!

<br>

From _Infinite Jest_ by David Foster Wallace:
>He won't take down Handle-Tie trashbags to clear the noise of being part of the neck. Gately imagines himself gathering this Wild Conceits guy totally strafed as he pictured himself with a dawdler's heavy tread the cement floor of Pat's screaming like water off a whole level of power the bad lads called me. They were right there, Boo, I'm starting to drop into its screen blinking ERROR at the front door and then P.E.T.

>The T at night, for the first time: then set your crosshairs and she is not a lob. It's a Boston colored thing on the note. His side up.

>His eyes crossing and uncrossing their legs apart and Lenz utilized akido to break your heart. She was pretty definitely an alcoholic and addict and burglar, not to overstep...

<br>

Of course, _Infinite Jest_ has some really strange passages (Wardine be cry), so weird results occur:

>Cartridge-fees went down with Wardine. Be give Wardine candy and 5s. Be stand in the shattuck suffer from excessive want, fear, censorship of speech and thought.

<br>



_Ulysses_ by James Joyce begins to sound more like _Finnegan's Wake_:
>You there. Catch aholt. Caraway seed to carry away. Twig?

>Poor story to tell you? As true as you’re there. O, commend me to fly in his free left hand under her nape, you’ll toss me all. O wonder! Coolsoft with ointments her hand crushed by old Tom Wall’s son. His first bow to the centrifugal departer? By inserting the.

<br>

From _War and Peace_ by Leo Tolstoy
>She is offended by the sound of the impending danger. Formerly, when going into action, gentlemen! Mack has surrendered with his hands. In their narration events occur solely by!

> Geographical and economic conditions, then the words of abuse, dreadful words, ejaculated one after another in silence, nodded with approval or shook his head and began sobbing, with tears!

<br>

I've gotten the most consistently "normal"-sounding output from _War and Peace_.

Usage
-----

Process:

* The first step is building the chains of words, which is simply a Python dictionary of word pairs and a list of all words that follow that specific pair. Rather than rebuild this each time text is requested to be generated, `to_json.py` dumps a Python dictionary object into a JSON file so the table is built exactly once. It's done like so: 
 
```bash
$ python3 to_json.py -f <input.txt> -o <output.json>
```

* With the Python object precomputed and saved, `markov.py` can generate text from the JSON like so:
```bash
$ python3 markov.py -f <output.json> -wc <desired word count>
```

Sample texts
------------

I've included some text files for some books that are in the public domain as well as their JSONified markov-chained versions.

Related
-------
[\-\-\-](https://github.com/patjm1992/infinite-ipsum)

Issues/To-Do
------

* Handling errant 'smart quotes' and parentheticals
* Handling chapter titles
* Optional write output text to file
* Passing in multiple text files