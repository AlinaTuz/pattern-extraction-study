# Hogwarts Quests - Assignment 2

### You are tracking the distance to the Hogwarts Express. A magical instrument reports it’s 100 leagues away. Before the reading, your belief about the distance $D$ was a Gaussian $D ∼ N(μ = 98, σ^2 = 16)$. The instrument’s reading is the true distance plus Gaussian noise $(N(0, 4))$.

#### a. What is the PDF of your prior belief of the train’s true distance?
The PDF of a Gaussian distribution
$$
f(d) = \frac{1}{\sqrt{2 \pi σ^2}}exp(-\frac{(d - μ)^2}{2σ^2})
$$
$$
f(d) = \frac{1}{\sqrt{2 \pi \times 16}}exp(-\frac{(d - 98)^2}{2\times 16}) = \frac{1}{4\sqrt{2 \pi}}exp(-\frac{(d - 98)^2}{32})
$$

---

#### b. What is the probability density of seeing a reading of 100 leagues, given the true distance is t?
$R$ will be the reading of the instrument and $T$ will be the true distance. The reading is the true distance plus some noise where the noise follows a Gaussian distribution with mean 0 and variance 4. This can be written as $R=T \times ϵ$ where $ϵ∼N(0,4)$.

We want to find the probability density of seeing this reading given the true distance is t. This is the likelihood function $P(R=100∣T=t)$. The reading R follows a Gaussian distribution with mean t and variance 4, $R∣T=t∼N(t,4)$.

 The PDF of $R$ given $T=t$ 
 $$
 f(r|t) = \frac{1}{\sqrt{2 \pi \times 4}}exp(-\frac{(r - t)^2}{2 \times 4})
 $$

In the case where r=100 we substitute this value into the PDF
 $$
 f(100|t) = \frac{1}{2\sqrt{2\pi}}exp(-\frac{(100 - t)^2}{8})
 $$


---

#### c. What is the PDF of your posterior belief (after the reading) of the train’s true distance? (You can leave a constant and don’t need to simplify).
The posterior PDF f(d∣100) is proportional to
$$
f(d∣100) ∝ f(100∣d) \times f(d)
$$
$$
f(d∣100) ∝ (\frac{1}{4\sqrt{2 \pi}}exp(-\frac{(d - 98)^2}{32})) \times (\frac{1}{2\sqrt{2\pi}}exp(-\frac{(100 - d)^2}{8}))
$$
$$
f(d∣100) ∝ exp(-\frac{(d - 98)^2}{32} -\frac{(100 - d)^2}{8})
$$
 
The constant will be the normalization factor that makes the integral of the PDF over all possible values of $d$ equal to 1.

---

### 2. On average, 5.5 owls arrive at the Owlery per minute. What is the probability that:

#### a. More than 7 owls will arrive in the next minute?
The probability that more than 7 owls will arrive in the next minute is $P(X > 7)$. We can use the Poisson distribution for this problem.
$$
P(X = k) = \frac{e^{-λ}λ^k}{k!}
$$
$$
P(X > 7) = 1 - P(X <= 7)
$$
$$
P(X <= 7) = \sum_{k = 0}^{7}p(X = k) = \sum_{k = 0}^{7} \frac{e^{-5.5}5.5^k}{k!} \approx 0.8094
$$
Then the probability $P(X > 7)$
$$
P(X > 7) = 1 - P( X <= 7) \approx 1 - 0.8094 \approx 0.1905
$$
**0.1905** the probability that more than 7 owls will arrive in the next minute.

---
#### b. More than 13 owls will arrive in the next 2 minutes?
The average number of owls arriving in 2 minutes is $λ \times 2 = 11$, $P(X > 13)$
We calculated $P(X <= 13)$ using the Poisson distribution with $λ = 11$
$$
P(X <= 13) = \sum_{k = 0}^{13} \frac{e^{-11}11^k}{k!} \approx 0.7812
$$
Then the probability $P(X > 13)$
$$
P(X > 13) = 1 - P( X <= 13) \approx 1 - 0.7812 \approx 0.2187
$$
**0.2187** the probability that more than 13 owls will arrive in the next 2 minutes.

---
#### c. More than 15 owls will arrive in the next 3 minutes?
The average number of owls arriving in 3 minutes is $λ \times 3 = 16.5$, $P(X > 15)$
We calculated $P(X <= 15)$ using the Poisson distribution with $λ = 16.5$
$$
P(X <= 15) = \sum_{k = 0}^{15} \frac{e^{-16.5}16.5^k}{k!} \approx 0.4180
$$
Then the probability $P(X > 15)$
$$
P(X > 15) = 1 - P( X <= 15) \approx 1 - 0.4180 \approx 0.5820
$$
**0.5820** the probability that more than 15 owls will arrive in the next 3 minutes.

---

### 3. The median of a continuous random variable (like the height of a gnome) having cumulative distribution function $F$ is the value $m$ such that $F(m) = 0.5$. Find the median of $X$ (in terms of distribution parameters) if:

#### a. $X ∼ Uni(a, b)$ (Uniform distribution, like the spread of Floo powder).
The cumulative distribution function (CDF) of a uniform distribution $X∼Uni(a,b)$ is
$$
F(x) =
\begin{cases} 
0, & x < a \\
\frac{x - a}{b - a}, & a \leq x \leq b \\
1, & x > b
\end{cases}
$$
The median m is the value $F(m)=0.5$. Since the median must be in the interval $[a, b]$ we can use the expression for $F(x)$ in this interval.
$$
F(m) = \frac{m - a}{b - a}
$$
The definition of $F(x)$ for $a <= x <= b$
$$
\frac{m - a}{b - a} = 0.5
$$
$$
m = \frac{a + b}{2}
$$

---
#### b. $X ∼ N(μ, σ^2)$ (Normal distribution, like scores on the O.W.L.s).
The cumulative distribution function (CDF) of a normal distribution $X ∼ N(μ, σ^2)$ is
$$
F(x) = P(X <=  x) = \int_{-\infty}^x \frac{1}{σ \sqrt{2\pi}} e^{-\frac{1}{2}(\frac{t - μ}{σ})^2} dt
$$

The median $m$ is the value such that $F(m) = 0.5$.
$$
\int_{-\infty}^m \frac{1}{σ \sqrt{2\pi}} e^{-\frac{1}{2} ( \frac{t - μ}{σ} )^2} dt = 0.5
$$

$Z = \frac{X-μ}{σ}$ will be the standard normal random variable with CDF $\Phi(z)$. Then $F(x) = \Phi(\frac{x - μ}{σ})$. We need to find $m$. 
$$
\Phi(\frac{m - μ}{σ}) = 0.5
$$

Since the standard normal distribution is symmetric around 0, $\Phi(0) = 0.5$.
$$
\frac{m-μ}{σ} = 0
$$
$$
m-μ = 0
$$
$$
m = μ
$$

---

### 4. Let $X_i$ be the number of students visiting the Hogwarts library in week $i$, where $X_i ∼ N(2200, 52900)$. Assume weekly visits $X_i$ are independent.

#### a. What is the probability that the total number of visitors in the next two weeks exceeds 5000?
Let $X_1, X_2 \sim N(2200, 52900)$ be the number of students visiting the library in each of the next two weeks. Since the visits are independent and normally distributed their sum is also normally distributed.
$$
X_1 + X_2 \sim N(2200 + 2200, 52900 + 52900) = N(4400, 105800)
$$

We want to find the probability that the total number of visitors in the next two weeks more than 5000:

$$
P(X_1 + X_2 > 5000)
$$

This is a probability about a normal variable so we standardize it to a standard normal variable.
$$
P(X_1 + X_2 > 5000) = P(Z > \frac{5000 - 4400}{\sqrt{105800}})
$$

$$
= P(Z > \frac{600}{\sqrt{105800}}) \approx P(Z > \frac{600}{325.3}) \approx P(Z > 1.845)
$$

$$
P(Z > 1.845) = 1 - \Phi(1.845) \approx 1 - 0.9675 \approx 0.0325
$$

**0.0325** is the probability that the total number of visitors in the next two weeks exceeds 5000.

---

#### b. What is the probability that the weekly number of visitors exceeds 2000 in at least 2 of the next 3 weeks?
Let $( X )$ be the number of visitors in a single week so $X \sim N(2200, 52900)$.  
The mean is $μ = 2200$ and the standard deviation is $( σ = \sqrt{52900} = 230 )$.

We want to find $P(X > 2000)$. We standardize $X$:
$$
Z = \frac{X - μ}{σ} = \frac{2000 - 2200}{230} = \frac{-200}{230} = -\frac{20}{23} \approx -0.8696
$$

$$
P(X > 2000) = P(Z > -0.8696) = 1 - P(Z \leq -0.8696) = P(Z \leq 0.8696)
$$
$$
P(Z \leq 0.8696) \approx 0.8078
$$

$p = P(X > 2000) \approx 0.8078$.

We are looking for the probability that this event occurs in at least 2 weeks of the next 3 weeks. This is a binomial probability problem with $n = 3$ trials (weeks) and success probability $p \approx 0.8078$. Let $Y$ be the number of weeks with more than 2000 visitors.  
$$
P(Y \geq 2) = P(Y = 2) + P(Y = 3)
$$

The probability mass function of a binomial distribution:
$$
P(Y = k) = \binom{n}{k} p^k (1 - p)^{n - k}
$$

For $Y = 2$:
$$
P(Y = 2) = \binom{3}{2} (0.8078)^2 (0.1922)^1 = 3 \cdot (0.65254) \cdot (0.1922) \approx 3 \cdot 0.12541 \approx 0.37623
$$

For $Y = 3$:
$$
P(Y = 3) = \binom{3}{3} (0.8078)^3 (0.1922)^0 = 1 \cdot (0.52726) \cdot 1 = 0.52726
$$
$$
P(Y \geq 2) = P(Y = 2) + P(Y = 3) \approx 0.37623 + 0.52726 \approx 0.9035
$$

**0.9035** is the probability that the weekly number of visitors exceeds 2000 in at least 2 of the next 3 weeks.

---
### 5. Let $X$, $Y$, and $Z$ be independent random variables representing the magical power levels of three Hogwarts students, where $X ∼ N(μ_1, σ_1^2)$ (Gryffindor), $Y ∼ N (μ_2, σ_2^2)$ (Hufflepuff), and $Z ∼ N(μ_3, σ_3^2)$ (Ravenclaw).

#### a. Let $A = X + Y$. What is the distribution of the combined power A?
$X$ and $Y$ are independent normal random variables their sum $A$ is also normally distributed.
$$
μ_A = E[A] = E[X + Y] = E[X] + E[Y] = μ_1 + μ_2
$$

The variance of $A$ is the sum of the variances of $X$ and $Y$ (due to independence).
$$
σ_A^2 = Var(A) = Var(X + Y) = Var(X) + Var(Y) = σ_1^2 + σ_2^2
$$

The distribution of the combined power $A$.
$$
A ∼ N(μ_1 + μ_2, σ_1^2 + σ_2^2)
$$
---
#### b. Let $B = 5X + 2$. What is the distribution of B (perhaps after a powerenhancing charm)?
Since $X$ is a normal random variable any linear transformation of $X$ will also be normally distributed. If $X ∼ N(μ_1, σ_1^2)$ then for a linear transformation $B = aX + b$ the distribution of $B$ is $N(aμ_1 + b,a^2σ_1^2)$

In this case a=5 and b=2.

The mean and variance of B:
$$
μ_B = E[B] = E[5X + 2] = 5E[X] + 2 = 5μ_1 + 2
$$
$$
σ_B^2 = Var(B) = Var(5X + 2) = 5^2Var(X) = 25σ_1^2
$$

The distribution of $B$:
$$
B ∼ N(5μ_1 + 2, 25σ_1^2)
$$
---
#### c. Let $C = aX − bY + c_2Z$, where $a$, $b$, and $c$ are real-valued constants representing spell modifiers. What is the distribution (and parameters) for $C$? Show how you derived your answer.
$X$, $Y$, and $Z$ are independent normal random variables, any linear combination of them is also normally distributed.

The mean and variance of C:
$$
E[C] = E[aX - bY + cZ] = aE[X] - bE[Y] + cE[Z] = aμ_1 - bμ_2 + cμ_3
$$
$$
Var(C) = Var(aX - bY + cZ) = Var(aX) + Var(-bY) + Var(cZ) = 
$$
$$
= a^2Var(X) - b^2Var(Y) + c^2Var(Z) = a^2σ_1^2 + b^2σ_2^2 + c^2σ_3^2
$$
The distribution of $C$:
$$
C ∼ N(aμ_1 - bμ_2 + cμ_3, a^2σ_1^2 + b^2σ_2^2 + c^2σ_3^2)
$$

---

### 6. The joint probability density function of continuous random variables $X$ (skill in Potions) and $Y$ (skill in Charms) is given by $f_{X,Y} (x, y) = c\frac{y}{x}$ where $0 < y < x < 1$.
#### a. What is the value of $c$ for this to be a valid probability density function?
The integral of $f_{X,Y}$ over the region where it is non-zero must be equal to 1. The region is R = {(x, y) ∣ 0 < y < x < 1}. We can set up the integral as:
$$
\iint_R c \frac{y}{x} \, dy \, dx = 1 
$$
We can integrate with respect to $y$ first then $x$. The limits of integration are $0 < x < 1$ and $0 < y < x$
$$
\int_{0}^{1} \int_{0}^{x} c \frac{y}{x} \, dy \, dx = 1 
$$
The inner integral:
$$
\int_{0}^{x} c \frac{y}{x} \, dy = \frac{c}{x} \int_{0}^{x} y \, dy = \frac{c}{x}\times \frac{y^2}{2} = \frac{c}{x} \times \frac{x^2}{2} = \frac{c x}{2}
$$
The outer integral:
$$ 
\int \frac{c x}{2} \, dx = \frac{c}{2} \int_{0}^{1} x \, dx = \frac{c}{2} \times [ \frac{x^2}{2} ]_{0}^{1} = \frac{c}{2} \times \frac{1}{2} = \frac{c}{4} 
$$
$$ 
\frac{c}{4} = 1 
$$
$$
c = 4
$$
**4 is the value of $c$** for this to be a valid probability density function.

---

#### b. Are Potion skill $(X)$ and Charm skill $(Y)$ independent? Explain.
Potion skill (X) and Charm skill (Y) are not independent.

Two random variables $X$ and $Y$ are independent if their joint probability density function $f_{X,Y}(x,y)$ can be written as the product of their marginal probability density functions $f_X(x)f_Y(y)$ for all $x$ and $y$.

The joint probability density function:
$$
f_{X,Y}(x, y) = 
\begin{cases}
4 \dfrac{y}{x}, & \text{if } 0 < y < x < 1 \\
0, & \text{otherwise}
\end{cases}
$$

The region where the joint PDF is non-zero (the support of the joint distribution) is the triangle in the xy-plane defined by $0 < y < x < 1$. This region is bounded by $y = 0$, $y = x$, and $x = 1$ in the first quadrant.

If $X$ and $Y$ were independent the support of their joint distribution would have to be a rectangle in the xy-plane, formed by the Cartesian product of the supports of the individual random variables $X$ and $Y$.

---

#### c. What is the marginal density function of $X$?
The marginal density function of $X$, $f_X(x)$ is found by integrating the joint PDF $f_{X,Y}(x,y)$ over all possible values of y.
$$ 
f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x, y) \, dy 
$$

For a given $x$ the joint PDF $f_{X,Y}(x, y)$ is non-zero only when $0 < y < x$.  
This means $x$ must also satisfy $0 < x < 1$ since $y > 0$ and $x < 1$.

For $0 < x < 1$ the marginal density of $X$:
$$
f_X(x) = \int_{0}^{x} 4  \frac{y}{x} \, dy
$$

$$
f_X(x) = \frac{4}{x} \int_{0}^{x} y \, dy = \frac{4}{x} \left[ \frac{y^2}{2} \right]_{0}^{x} = \frac{4}{x} \times \frac{x^2}{2} = 2x
$$

If $x$ is not in the interval $(0, 1)$, then $f_{X,Y}(x, y) = 0$ for all $y$: $f_X(x) = 0$.


The marginal density function of $X$:
$$
f_X(x) = 
\begin{cases}
2x, & \text{if } 0 < x < 1 \\
0, & \text{otherwise}
\end{cases}
$$
---

#### d. What is the marginal density function of $Y$?

The marginal density function of $Y$, $f_Y(y)$ is found by integrating the joint PDF $f_{X,Y}(x, y)$ over all possible values of $x$.

$$
f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x, y) \, dx
$$

For a given $y$, $f_{X,Y}(x,y)$ is non-zero only when $y < x < 1$.  
This requires $0 < y < 1$. The marginal density of $Y$:

$$
f_Y(y) = \int_{y}^{1} 4  \frac{y}{x} \, dx
$$
$$
f_Y(y) = 4y \int_{y}^{1} \frac{1}{x} \, dx = 4y [ \ln|x|]_{y}^{1}
$$

Since $y > 0$ we can drop the absolute value and use $\ln(x)$:

$$
f_Y(y) = 4y (\ln(1) - \ln(y)) = 4y (0 - \ln(y)) = -4y \ln(y)
$$

If $y$ is not in the interval $(0, 1)$ then $f_{X,Y}(x,y) = 0$ for all $x$: $f_Y(y) = 0$.

The marginal density function of $Y$:
$$
f_Y(y) = 
\begin{cases}
-4y \ln(y), & \text{if } 0 < y < 1 \\
0, & \text{otherwise}
\end{cases}
$$

---

### 7. Choose a number X at random from the set of house points {1, 2, 3, 4, 5, 6} awarded by Professor McGonagall. Now choose a number $Y$ at random from the subset of points no larger than $X$, {1, . . . ,X}.
#### a. Determine the joint probability mass function of $X$ (initial points) and $Y$ (second random selection).
The joint probability mass function of $X$ and $Y$ is given by
$$
P(X = x, Y = y) = P(Y = y \mid X = x) \times P(X = x)
$$

The random variable $X$ is chosen from the set $\{1,2,3,4,5,6\}$ with uniform probability. The probability mass function of $X$:
$$
P(X = x) = \frac{1}{6} \quad \text{for } x \in \{1,2,3,4,5,6\}.
$$

Given a value of $X = x$ the random variable $Y$ is chosen from the subset $\{1,2,\dots,x\}$ with uniform probability.  
The conditional probability mass function of $Y$ given $X = x$:
$$
P(Y = y \mid X = x) = \frac{1}{x} \quad \text{for } y \in \{1,2,\dots,x\}.
$$

The joint probability mass function of $X$ and $Y$:
$$
P(X = x, Y = y) = P(Y = y \mid X = x) \times P(X = x) = \frac{1}{x} \times \frac{1}{6} = \frac{1}{6x}
$$

The joint PMF:
$$
P(X = x, Y = y) =
\begin{cases}
\frac{1}{6x}, & \text{if } x \in \{1,2,3,4,5,6\} \text{ and } 1 \leq y \leq x \\
0, & \text{otherwise}
\end{cases}
$$

---

#### b. Determine the conditional mass function $P(X = j|Y = i)$ as a function of $i$ and $j$.
We can use the definition of conditional probability:
$$
P(X = j \mid Y = i) = \frac{P(X = j, Y = i)}{P(Y = i)}
$$

We can find the marginal probability mass function of $Y$ by summing the joint probability over all possible values of $X$:

$$
P(Y = i) = \sum_{j = i}^{6} P(X = j, Y = i)
$$

For a given value of $i$ the possible values of $j$ are those for which $j => i$ and $j \in \{1, 2, 3, 4, 5, 6\}$. So the sum is over $j$ from $i$ to 6:

$$
P(Y = i) = \sum_{j = i}^{6} \frac{1}{6j} = \frac{1}{6}\sum_{j = i}^{6} \frac{1}{j}
$$

Now we can substitute the expressions for $P(X = j, Y = i)$ and $P(Y = i)$ into the formula for conditional probability:

$$
P(X = j \mid Y = i) = \frac{P(X = j, Y = i)}{P(Y = i)} = \frac{\frac{1}{6j}}{\frac{1}{6}\sum_{k = i}^{6} \frac{1}{k}}
$$

We used $k$ as the index of summation.We can simplify this expression by canceling out the $\frac{1}{6}$ terms:

$$
P(X = j \mid Y = i) = \frac{\frac{1}{j}}{\sum_{k = i}^{6} \frac{1}{k}}
$$

This conditional probability is defined for $i \in \{1, 2, 3, 4, 5, 6\}$ and $j \in \{i, i+1, \dots, 6\}$. If $j < i$ then $P(X = j, Y = i) = 0$ so $P(X = j \mid Y = i) = 0$.

Thus the conditional mass function $P(X = j \mid Y = i)$ is

$$
P(X = j \mid Y = i) =
\begin{cases}
\frac{\frac{1}{j}}{\sum_{k = i}^{6} \frac{1}{k}}, & \text{if } j \in \{i, i+1, \dots, 6\} \text{ and } i \in \{1, 2, 3, 4, 5, 6\} \\
0, & \text{otherwise}
\end{cases}
$$

---

#### c. Are $X$ and $Y$ independent? Explain.
X and Y are not independent

Two random variables $X$ and $Y$ are independent if the chance of both $X$ and $Y$ happening at the same time is the chances of each one happening on its own:
$$
P(X = x, Y = y) = P(X = x) \times P(Y = y)
$$

$X$ and $Y$ are independent if the conditional probability of one variable given the other is equal to the marginal probability of the first variable:
$$
P(X = j \mid Y = i) = P(X = j) \ or \ P(Y = i \mid X = j) = P(Y = i)
$$

We found the conditional probability mass function. From the problem we know the marginal probability mass function of $X$:

$$
P(X = j) = \frac{1}{6} \quad \text{for } j \in \{1, 2, 3, 4, 5, 6\}.
$$

For $X$ and $Y$ to be independent, we would need:

$$
\frac{\frac{1}{j}}{\sum_{k = i}^{6} \frac{1}{k}} = \frac{1}{6}
$$

We can compute $P(X = 1 \mid Y = 1)$:

$$
P(X = 1 \mid Y = 1) = \frac{\frac{1}{1}}{\sum_{k = 1}^{6} \frac{1}{k}} = \frac{1}{1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6}}
$$

Evaluating the sum:
$$
P(X = 1 \mid Y = 1) = \frac{1}{1 + 0.5 + 0.3333 + 0.25 + 0.2 + 0.1667} = \frac{1}{2.45}
$$

$$
P(X = 1 \mid Y = 1) = \frac{49}{147}
$$

Since $\frac{49}{147} \neq \frac{1}{6}$ the condition for independence is not met.
