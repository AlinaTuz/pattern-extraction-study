# The Reichenbach Reckoning: Sherlock Holmes’ Mathematical Mysteries 

These quests are infused with the atmosphere of Victorian mystery, deductive reasoning, and the intrigue of 221B Baker Street. The problems are now framed as cases or puzzles Holmes and Watson might encounter, requiring clever twists and contextual reasoning.

## 1 Written Problems 
### 1. The Seating of the Diogenes Club 

Sherlock Holmes investigates a clandestine meeting at the Diogenes Club, where 10 distinct members must sit in a row under strict protocols:

#### a. If no rules bind their arrangement, how many ways can the silent gentlemen be seated?

With no restrictions on the seating arrangement, each member is distinct, and thus the number of ways to seat the 10 members is 

$$
10! = 3628800
$$

**3628800 ways** can the silent gentlemen be seated

---

#### b. Suppose Mycroft Holmes and his aide, bound by mutual distrust, must sit side-by-side to monitor each other—how many arrangements are possible?

First we should treat Mycroft Holmes and his aide as one combined unit. This reduces the problem to arranging 9 units (8 members and the Mycroft-aide unit), then arrangment will be 9!. And inside the unit there are 2 possible internal arrangements.

$$
9! \times 2 = 725760
$$

**725760 arrangements** are possible

---

### c. If 5 are seasoned inspectors and 5 are novice constables, and no two of the same rank may sit adjacent (lest rivalries flare), how many seating orders hold?

There are 6 gaps available (one before the first inspector, one after the last, and one between each pair). The 5 constables must occupy 5 out of these 6 gaps.

$$
5! \times 5! \times \binom{6}{5} = 86400
$$

**86400 seating arrangements** are possible.

---

### d. If the 10 form 5 pairs of informants and handlers, each pair inseparable due to whispered secrets, how many arrangements emerge?

5! to arrange 5 groups in a row, 2! to arrange the two people inside a single pair and 2 to the power of 5 accounts for all 5 groups because each pair's internal arrangement is independent of the others.

$$
5! \times 2^5 = 3,840
$$

**3840 arrangements** emerge.

---

*Deduction: Explain your reasoning as if briefing Watson on the club’s hidden hierarchy.*


## 2. The Cipher Arrays of Irene Adler

Irene Adler hides messages in sorted arrays of k distinct integers, each from 1 to n (e.g., 1 ≤ x[0] < x[1] < … < x[k-1] ≤ n). How many such arrays can she devise, as if concealing clues in a locked box?


We need to select k different numbers in such a way that they are in increasing order. To make an array, we select k elements from n without considering order.


$$
\binom{n}{k} = \frac{n!}{k!(n-k)!}
$$

**$\binom{n}{k}$ the number of arrays** she can create

---
*Deduction: Unravel the pattern as if outwitting her guile.*

## 3. The Paths of the Hound

A mechanical hound roams an n × m grid from (1,1) to (n,m), moving only right or down.

### a. With no bounds, how many trails can it leave?

The total number of steps required to move from (1,1) to (n,m) is:

$$
(n - 1) + (m - 1) = n + m - 2
$$

Since the movement consists of (m−1) right steps, and the rest are downward, the number of unique paths is given by the binomial coefficient:

$$
\binom{n+m-2}{m-1}
$$

---

### b. If it must first lurch right (a faulty gear), how many paths remain?

The new starting position is (1,2), meaning one right move is already taken. The remaining steps are:

$$
(n - 1) + (m - 2) = n + m - 3
$$

Thus, the number of remaining paths is:

$$
\binom{n+m-3}{m-2}
$$

---

### c. If it switches direction exactly thrice (right-to-down or down-to-right), how many routes obey?


We start in direction $( d \in \{ \text{right}, \text{down} \} )$, and $(d')$ is the other direction. Then, $(k)$ turns means that there are $(1 + \left\lfloor \frac{k}{2} \right\rfloor)$ contiguous segments in direction $( d)$, and $(\left\lceil \frac{k}{2} \right\rceil)$ segments in direction $( d')$. The entire sequence of moves is specified if we specify how many moves there are in each of these segments. That is, let $( x_1, x_2, \dots, x_1 + \left\lfloor \frac{k}{2} \right\rfloor)$ be the numbers of moves in the segments in direction $(d)$, and each of $( y_1, y_2, \dots, y_{\left\lceil \frac{k}{2} \right\rceil})$ be the number of moves in the segments in direction $( d')$. Then the entire path is completely determined by the $( x_i)$'s and $( y_j)$'s.

$k = 3$ for 3 direction switches.

As the number of total number of moves in each direction is \( n-1 \), we are looking (for each choice of \( d \)) for the number of positive integer solutions to:

$$
x_1 + x_2 + \dots + x_{\left\lceil 1 + \frac{k}{2} \right\rceil} = n - 1
$$

$$
y_1 + y_2 + \dots + y_{\left\lceil \frac{k}{2} \right\rceil} = n - 1
$$

This gives the final answer as:

$$
2 \times \binom{m-2}{\frac{k}{2}} \times \binom{m-2}{\frac{k}{2}-1}
$$

---

*Deduction: Track its steps as if hunting it across the moors.*


## 4. The Poker Game at Reichenbach

Holmes faces Moriarty at a poker table, where all 5-card hands from a 52-card deck are equally likely:

### a. What’s the chance of a flush (all same suit), including straight flushes?

We start by counting the total number of 5-card hands. There are 52 cards in the deck, and we need to choose 5:

$$
\binom{52}{5} = \frac{52!}{5!(52-5)!} = 2598960
$$

Now, a flush consists of 5 cards of the same suit. Since there are 4 suits (hearts, diamonds, clubs, spades), we calculate the number of ways to choose 5 cards from the 13 available in each suit:

$$
\binom{13}{5} = \frac{13!}{5!(13-5)!} = 1287
$$

Since we can have a flush in any of the 4 suits, the total number of flush hands (including straight flushes) is:

$$
4 \times 1287 = 5148
$$

The probability of being dealt a flush (including straight flushes) is:

$$
P = \frac{5148}{2598960} \approx 0.00198
$$

The probability is about **0.198%**

---
### b. What’s the chance of two pairs (a, a, b, b, c, distinct values)?  

To form a two-pair hand, we first choose two different ranks for the pairs. There are 13 ranks, and we select 2 of them:  

$$
\binom{13}{2} = 78
$$  

For each chosen rank, we need to pick 2 out of 4 suits, which gives:  

$$
\binom{4}{2} = 6
$$ 

Since we have two pairs, we do this twice:  

$$
6 \times 6 = 36
$$

Next, we need to select a fifth card of a different rank (not matching the two pairs). There are 11 remaining ranks (13 total minus the 2 chosen), and we pick 1:  

$$
\binom{11}{1} = 11
$$  

For this card, we choose any one of the 4 suits:  

$$
\binom{4}{1} = 4
$$ 

Multiplying these choices together gives the number of two-pair hands:  

$$
78 \times 36 \times 11 \times 4 = 123552
$$ 

Dividing by the total number of hands:  

$$
P = \frac{123552}{2598960} \approx 0.0475
$$  

The probability is about **4.75%**  

---  

### c. What’s the chance of four of a kind (a, a, a, a, b, distinct)?  

To form a four-of-a-kind hand, we first choose a rank for the four matching cards. There are 13 possible ranks:  

$$
\binom{13}{1} = 13
$$

Since we must take all four suits of this rank, there is only 1 way to do so.  

Next, we choose a different rank for the kicker (the extra card). There are 12 remaining ranks:  

$$
\binom{12}{1} = 12
$$ 

For this kicker, we choose one of the 4 suits:  

$$
\binom{4}{1} = 4
$$

Multiplying these choices together gives the number of four-of-a-kind hands:  

$$
13 \times 1 \times 12 \times 4 = 624
$$

Dividing by the total number of hands:  

$$
P = \frac{624}{2598960} \approx 0.00024
$$ 

The probability is about **0.024%**  

---  

*Deduction: Compute the odds as if spotting Moriarty’s bluff.*


## 5. The Binary Telegram of Baskerville

A telegraph sends M 0’s and N 1’s in random order. What’s the chance the first r bits hold exactly k 1’s, as if decoding a hound’s howl?

The total number of bits is ( M + N ).

The total number of successes (1's) in the population is N. We randomly choose r bits (without replacement) and then count how many of those r bits are 1's.

The probability of exactly k 1's in the first r bits is given by the hypergeometric probability formula:

$$
P(k) = \frac{\binom{N}{k} \binom{M}{r-k}}{\binom{M+N}{r}}
$$


$\binom{N}{k}$ the number of ways to choose k 1's from N 1's.

$\binom{M}{r-k}$ the number of ways to choose the remaining r-k 0's from M 0's.

$\binom{M+N}{r}$ the total number of ways to choose r bits from the total of ( M + N ) bits.

**$\frac{\binom{N}{k} \binom{M}{r-k}}{\binom{M+N}{r}}$ the chance the first r bits hold exactly k 1’s**

---

*Deduction: Reason through the static as if time is running out.*

## 6. The Menagerie of Moriarty

Holmes uncovers Professor Moriarty’s scheme to display 3 bird species and 3 reptile species, selected from 8 birds and 6 reptiles, in a sinister zoo:

### a. If Moriarty chooses freely, how many exhibits can he craft?

Moriarty is selecting 3 bird species from 8 birds and 3 reptile species from 6 reptiles. The number of ways to select the birds and reptiles is given by the combination formula:

$$
\binom{8}{3} \times \binom{6}{3} = \frac{8! \times 6!}{3!(8-3)! \times 3!(6-3)!} = 1120
$$

**1120 exhibits** can be crafted.

---

### b. Two birds—one a hawk with a piercing cry, the other a raven with a deadly glare—cannot coexist without chaos. How many exhibits avoid this peril?

First, let’s count how many exhibits will have chaos. If the hawk and raven are chosen, we need to select a third bird from the remaining birds (excluding hawk and raven). There are 6 birds left:

$$
\binom{6}{1} \times \binom{6}{3} = \frac{6! \times 6!}{(6-1)! \times 3!(6-3)!} = 120
$$

The number of forbidden exhibits is **120**. Now, subtract the forbidden cases from the total:

$$
1120 - 120 = 1000
$$

**1000 exhibits** avoid this peril.

---

### c. A venomous parrot and a cobra, when paired, unleash a toxic fog. How many exhibits dodge this trap?

Here the parrot and cobra are already chosen. Now we need to select the remaining birds and reptiles:

For the birds, there are 7 birds left after excluding the parrot.
For the reptiles, there are 5 reptiles left after excluding the cobra.

The number of exhibits that include the parrot and cobra is:

$$
\binom{7}{2} \times \binom{5}{2} = \frac{7! \times 5!}{2!(7-2)! \times 2!(5-2)!} = 210
$$

Now subtract the forbidden cases from the total:

$$
1120 - 210 = 910
$$

**910 exhibits** dodge this trap.

---

*Deduction: Justify your counts as if tracing Moriarty’s twisted logic.*

## 7. The Investments of Baker Street

Holmes secures £20 million to fund 4 shadowy enterprises, investing in £1 million units, each with a minimum stake: £1M, £2M, £3M, £4M.

### a. If all 4 must be funded to foil Moriarty’s network, how many strategies exist?

We first allocate the minimum stakes to each enterprise:

$$
1M + 2M + 3M + 4M = 10M
$$

With £10M allocated, we have:

$$
20M - 10M = 10M \quad \text{left to be distributed}
$$

Next we distribute the remaining £10M among the 4 enterprises. This is equivalent to finding the number of non-negative integer solutions to the equation, which is a **stars and bars** problem:

$$
\binom{10 + 4 - 1}{4 - 1} = \binom{13}{3} = 286
$$

**286 strategies** exist to fund the enterprises.

---

### b. If at least 3 must be backed (to keep the web intact), how many plans work?

- First enterprise: £10M
- Second enterprise: £12M
- Third enterprise: £13M
- Fourth enterprise: £14M

$$
First = \frac{11 + 3 - 1}{3 - 1} = \frac{13}{2} = 78
$$
$$
Second = \frac{12 + 3 - 1}{3 - 1} = \frac{14}{2} = 91
$$
$$
Third = \frac{13 + 3 - 1}{3 - 1} = \frac{15}{2} = 105
$$
$$
Fourth = \frac{14 + 3 - 1}{3 - 1} = \frac{16}{2} = 120
$$


Summing these cases:

$$
78 + 91 + 105 + 120 = 394
$$

**394 plans** work

---

*Deduction: Argue your totals as if pitching to a wary Watson.*

## 8. The Coding Conundrum of Scotland Yard  

Holmes probes a cryptography school where 100 agents study 3 courses—Java, C++, Python—under Lestrade’s watch:

Java: 27 agents; C++: 28; Python: 20.

12 crack Java and C++; 5 master Java and Python; 8 excel in C++ and Python.

2 prodigies conquer all three.

### a. What’s the chance a random agent has evaded all courses, lurking in the shadows?  

Using the principle of Inclusion-Exclusion, we calculate how many agents have taken at least one course.
 
- Java = J  
- C++ = C  
- Python = P 
 
Applying the Inclusion-Exclusion Principle:  

$$
|J \cup C \cup P| = |J| + |C| + |P| - |J \cap C| - |J \cap P| - |C \cap P| + |J \cap C \cap P| =
$$

$$
= 27 + 28 + 20 - 12 - 5 - 8 + 2 = 52
$$

Thus, the number of agents who haven’t taken any of the courses:  

$$
100 - 52 = 48
$$

The probability that a randomly chosen agent has evaded all courses:

$$
P = \frac{48}{100} = 0.48
$$

**48% the chance** a random agent has evaded all courses

---

### b. What’s the chance an agent studies exactly one, avoiding the others’ scrutiny?  

To solve this problem, we need to find the probability that an agent is taking exactly one of the math or psychology classes.  

The number of agents taking only Java is the number of agents taking Java minus the number of agents taking both Java and C++ and Java and Python and conquer all three:  
$$
27 – 12 – 5 – 2 = 8
$$  

The number of agents taking only C++ is the number of agents taking C++ minus the number of agents taking both Java and C++ and C++ and Python and conquer all three:  
$$
28 – 12 – 8 – 2 = 6
$$  

The number of agents taking only Python is the number of agents taking Python minus the number of agents taking both Java and Python and C++ and Python and conquer all three:  
$$
20 – 5 – 8 – 2 = 5
$$ 

The total number of agents taking exactly one class is the sum of the agents taking only Java and only C++ and only Python class:  
$$
8 + 6 + 5 = 19
$$  

The probability of an agent taking exactly one class is the number of agents taking exactly one class divided by the total number of agents:  
$$
P = \frac{19}{100} = 0.19 
$$  

**19% the chance** an agent studies exactly one course 

---

### c. If two agents are nabbed, what’s the odds at least one knows a course? Give a final number.  

To determine this, we first find the probability that an agent hasn't taken any course.
If two agents are nabbed, the probability that both have taken no course is:  

$$
P(\text{Both No Course}) = 0.48 \times 0.48 = 0.2304
$$

The probability that at least one of them has taken a course is the complement of this event:  

$$
P(\text{At Least One Course}) = 1 - P(\text{Both No Course}) = 1 - 0.2304 = 0.7696
$$  

Odds are calculated as the ratio of the probability of success to the probability of failure:  

$$
P = \frac{0.7696}{0.2304} = \frac{7696}{2304} \approx 3.34
$$ 

The odds **at least one knows a course 3.34** 

---

*Deduction: Map the overlaps as if decoding a Yard cipher—explain each step.*

## 9. The Passwords of the Naval Treaty

A spy tackles \( n \) distinct passwords, one unlocking a treaty:

### a. Trying randomly and discarding failures, what’s the chance the \(k\)-th attempt succeeds?

If the spy attempts passwords without repeating any, then each failed attempt removes one incorrect password. The first \(k-1\) attempts must be failures. The probability of the treaty password appearing on the \(k\)-th try follows a conditional probability:

$$
P(X = k) = \frac{1}{n-k+1}
$$

Only \( n-k+1 \) passwords remain by the \( k \)-th attempt.
The spy selects randomly among the remaining options.

---

### b. Trying randomly without discarding, stopping at success, what’s the chance the \(k\)-th try wins?

If the spy retries passwords randomly and stops upon success, this follows a geometric distribution:

$$
P(X = k) = (1 - \frac{1}{n})^{k-1} \times \frac{1}{n}
$$

$(1 - \frac{1}{n})^{k-1}$ is the probability of failing \( k-1 \) times.

$\frac{1}{n}$ is the probability of succeeding on the \( k \)-th attempt.

---

*Deduction: Think like the spy—explain as if Holmes is one step ahead.*


## 10. The Dice of the Speckled Band

Holmes rolls a six-sided die six times to crack a gypsy code.

### a. What’s the chance two numbers appear thrice each (e.g., three 4s, three 6s)?

Each die roll has 6 possible outcomes, and since we roll **6 times**, the total number of possible sequences is:

$$
6^6
$$

We need exactly two distinct numbers, so we choose 2 numbers from {1, 2, 3, 4, 5, 6}:

$$
\binom{6}{2} = 15
$$

Once we have picked our two numbers, we need to distribute them across the 6 rolls so that each number appears exactly 3 times:

$$
\binom{6}{3} = 20
$$

Thus the total number of ways to achieve this outcome is:

$$
15 \times 20 = 300
$$

Since the total number of dice sequences is $(6^6)$, the probability is:

$$
P = \frac{300}{6^6} \approx 0.00643
$$

**About 0.643% is the chance two numbers appear thrice.**

---

### b. What’s the chance exactly one number hits thrice, no more, no less?

We first select one number from {1, 2, 3, 4, 5, 6}:

$$
\binom{6}{1} = 6
$$

Since we've already chosen one number, we pick 3 distinct numbers from the remaining 5:

$$
\binom{5}{3} = 10
$$

Since these numbers are distinct, they can be arranged in $(3!)$ ways:

$$
3! = 6
$$

The total number of favorable outcomes is:

$$
6 \times 20 \times 10 \times 6 = 7200
$$

The probability is:

$$
P = \frac{7200}{6^6} \approx 0.1543
$$

**About 15.43% is the chance exactly one number hits thrice.**

---

*Deduction: Interpret the rolls as if they spell a fatal clue—mind the overlaps.*

## 11. The Letters of the Red-Headed League

Holmes dispatches 20 distinct letters to 12 unique informants, each landing randomly. What’s the chance 4 get exactly 2 letters and 3 get exactly 4, the rest empty-handed?

Each letter is assigned independently and uniformly to one of the 12 informants. The probability distribution follows a multinomial model, where we count how many letters each informant receives.

$(X_i)$ as the number of letters received by informant $(i)$, where:

$$
X_i \sim \text{Multinomial}(20, \frac{1}{12}, \frac{1}{12}, \dots, \frac{1}{12})
$$

We seek the probability that:

- 4 informants receive exactly 2 letters.
- 3 informants receive exactly 4 letters.
- The remaining 5 informants receive 0 letters.

The probability of this specific allocation is given by:

$$
P = \frac{20!}{(2!)^4 (4!)^3 (0!)^5} \times \left( \frac{1}{12} \right)^{20}
$$

$\frac{20!}{(2!)^4 (4!)^3 5!}$ counts the number of ways to assign letters.

$\left( \frac{1}{12} \right)^{20}$ accounts for the probability of each assignment.

---

*Deduction:  Trace the mail as if thwarting a league plot.*


## 12. The Buckets of Bohemia

m clues are hashed into N buckets by a rogue algorithm, all $(N^m)$ outcomes equal. What’s the chance exactly k land in the first bucket?

Each of the m clues is hashed independently and uniformly into one of N buckets. That means each clue lands in any bucket with probability $(\frac{1}{N})$. Next clue lands in another bucket with probability $(1- \frac{1}{N})$.

We are placing m independent clues:

$(X)$ - number of clues landing in bucket 1

$$
(X \sim Bin(m, p=\frac{1}{N}))
$$

This is the probability mass function (PMF) of a binomial distribution:

$$
P(X = k) = \binom{m}{k} \left( \frac{1}{N} \right)^k \left( 1 - \frac{1}{N} \right)^{m-k}
$$

where:

$(\binom{m}{k})$ = ways to choose which k clues land in bucket 1.

$(\left( \frac{1}{N} \right)^k)$ = probability that those k clues go into bucket 1.

$(\left( 1 - \frac{1}{N} \right)^{m-k})$ = probability that the remaining $(m - k)$ clues go elsewhere.

---

*Deduction: Model the scatter as if piecing together a broken photograph.*