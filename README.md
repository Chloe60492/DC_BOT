# BBC-discord bot

## Environment Setup

#### Exactly the same as TA's default

## File

#### Download
* git clone: https://github.com/Chloe60492/DC_BOT.git
* B08404023.zip

#### python file:

* `main.py`
* `basic_feature.py`
* `extra_feature.py`


## RUN & FUNCTION


### Excutate `main.py` file
#### if it suceeds then you will see `Bot is online!` and login message in your terminal. 


### Input the following commands in the dialog box

#### Basic features
* `!hello`
    * Input: `!hello`
    * Bot reply: 
        * The first greeting: `Hello {member.name}~`
        * Not the first greeting: `Hello {member.name}... This feels familiar.`
    * Example: ![](https://hackmd.io/_uploads/rJT3l9Orn.png)

* `!say`
    * Input: `!say "any word you want to say"`
    * Bot reply: repeat your words
    * Example:![](https://hackmd.io/_uploads/ByE-Z5drh.png)

* `!prefix`
    * Input: `!prefix "any punctuation"`
    * Bot reply:
        * `Command prefix has been set to "{new_prefix}"`
        * Then, we need to use new prefix to type all commands
    * Example: 
        ![](https://hackmd.io/_uploads/r1hXb9dH3.png)

* `!GPA`
    * Input: `!GPA "grading sequence with space between two grade "`
    * Bot reply: Calculate the average of the grading sequece we provided
    * Example:
        ![](https://hackmd.io/_uploads/S1VnJcOr3.png)


#### Extra features
* use `on_message` to monitor keywords and reply automatically
    * Input: any words including "thanks", "thank" or "thx"
    * Bot reply: 
        * randomly reply something like "You're welcome!"
        * react to our words with emoji🤗
    * Example:
        ![](https://hackmd.io/_uploads/By19_cdHn.png)

* `!helper`
    * Input: `!helper`
    * Bot reply: show all commands of the bot and how they work with embed messages
    * Example:
        ![](https://hackmd.io/_uploads/ByIuq5dr2.png)
![](https://hackmd.io/_uploads/ByxK5qdr3.png)

* `!food`
    * Input:`!food`
    * Bot reply: provide two button link to two common food delivery websites
    * Example:
        ![](https://hackmd.io/_uploads/rkK-VsOBh.png)

* `!shop`
    * Input:`!shop`
    * Bot reply: provide three button link to two common online shopping websites
    * Example:
        ![](https://hackmd.io/_uploads/BkZ7NsOBn.png)
