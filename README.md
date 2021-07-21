# Investment is good for charitable donations

This is a minor project in which I show that there are great, non-selfish benefits to investing money you intend to give to charity. I consider a strategy in which you donate a small fraction of the assets intended for charity each year, while investing the rest. Click [here](https://github.com/rjwthree/Invest-donate/blob/main/InvestDonate.pdf) to read about the mathematical details and [here](https://github.com/rjwthree/Invest-donate/blob/main/InvestDonate.py) to see the Python functions I wrote that make it easy to calculate the results of any variant of the strategy.

&nbsp;

In this scenario we imagine an initial amount of disposable money, say $1,000, that we want to donate. Instead of doing so all at once, we can invest it and donate 1% at the end of each year. This plot shows how many years it would take to donate multiples of the original amount for various growth rates.

A realistic growth rate for the stock market, 10%, would allow someone to donate more than 20 times the original amount over 60 years. They would also have grown the original $1,000 investment to more than $166,000, which could be used for continued 1% donations, or donated as well for a total donation of more than $186,000. This is an impressive lifetime outcome for a mere $1,000.

We can also note the power of compounding growth: although it took 60 years to donate 20 times the original investment, it would take only another 8 years to do that again, and another 5 years to do it a third time.

<p align="center">
<img src="https://github.com/rjwthree/Invest-Donate/blob/main/InvestDonate.png" width="700" height="600"/>
</p>

&nbsp;

How would this approach fare with a higher donation rate like 3%? The first plot zooms in to make the differences visible; the second one shows the whole picture. What conclusions can we draw? At first, larger donations improve our cumulative donations, but eventually smaller donations overtake them. The differences matter much more if the growth rate is small. Even though the points at which 1% donations surpass 3% donations are not observed for growth rates of 15% and more, they exist for any growth rate. It takes 80 years for 1% donations to win at 5% growth; 67 years at 10% growth; and 58 years at 30% growth.

<p align="center">
<img src="https://github.com/rjwthree/Invest-Donate/blob/main/InvestDonate2.png" width="700" height="600"/>
</p>

<p align="center">
<img src="https://github.com/rjwthree/Invest-Donate/blob/main/InvestDonate3.png" width="700" height="600"/>
</p>


&nbsp;

### Reality check

Taxes are a major consideration in real life. Imagine a US citizen whose marginal federal and state tax rates sum to 28%. If this person doesn't donate money earmarked for charity in the year they earned it, then just to restore the pre-tax amount they would need a 39% gain (i.e., 0.72 × 1.39 = 1.00). This may seem to tarnish an idea that sounded nice in theory. It's a very important caveat, but there are two reasons why the idea can still be implemented in reality.

First, charitable donations do not reduce taxes significantly for everyone. If someone filing individually gave $10,000 to charities in 2021, they may still benefit most by taking the standard deduction of $12,550. In this case, they would be able to deduct only an additional $300 from their taxable income despite their generous donations being far larger. If their federal marginal tax rate were 22%, the donations would save them only $66 on federal taxes.

Second, some tax-advantaged accounts allow both contributions and investment earnings to escape income taxes. If some fraction of your contributions to a traditional IRA or 401(k) were mentally allocated to charity, you could pursue this approach without any concern for taxes and donate from the account. Tax-deferred retirement accounts present the ideal [location](https://www.fidelity.com/viewpoints/investing-ideas/asset-location-lower-taxes) for charity-focused investment.
