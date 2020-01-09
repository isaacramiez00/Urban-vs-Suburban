import matplotlib.pyplot as plt
import scipy.stats as stats
import matplotlib
import pandas as pd
import numpy as np


plt.style.use('ggplot')

# test
def ztest():

    h_null = urban_denver_df
    h_alt = suburbs_df

    mu = h_null['monthlyCashFlow'].mean()
    sigma = np.sqrt(h_null['monthlyCashFlow'].var())
    x_bar = h_alt['monthlyCashFlow'].mean()

    alpha = 0.05
    z = (x_bar - mu)/ sigma
    print(f'The Z statistic for suburban homes is {z:0.02f}.')

    dist = stats.norm(mu, sigma)
    totalMonthlyCashFlow = np.linspace(dist.ppf(0.01), dist.ppf(0.99), 100)
    pdf_monthlyCashFlow = dist.pdf(totalMonthlyCashFlow)

    fig, ax = plt.subplots(2, 1, figsize=(12,8))
    ax[0].plot(totalMonthlyCashFlow, pdf_monthlyCashFlow, label='Urban home mean monthly cash flow dist.')
    ax[0].axvline(x_bar, color='green', label='Suburban sample mean dist.')
    ax[0].legend(loc='best')
    ax[0].set_title('Comparison of urban homes and suburban homes population distribution.')
    ax[0].set_xlabel('Monthly Cash Flow')
    ax[0].set_ylabel('Pdf');
    plt.savefig('ztest_urban_vs_suburban_pdf.png')

    fig.subplots_adjust(hspace=0.9)

    p = 1 - dist.cdf(x_bar)
    print("The probaility of these results, or more extreme, given the \
           null hypothesis is true is {0:0.2f}".format(p))
    
    cdf_monthlyCashFlow = dist.cdf(totalMonthlyCashFlow)
    ax[1].plot(totalMonthlyCashFlow, cdf_monthlyCashFlow, label='Urban home mean monthly cash flow income.')
    ax[1].axvline(x_bar, color='green', label='Suburban home sample mean dist.')
    ax[1].legend(loc='best')
    ax[1].set_title('Cumulative Distribution.')
    ax[1].set_xlabel('Monthly Cash Flow')
    ax[1].set_ylabel('cdf');
    plt.savefig('ztest_urban_suburban_cdf.png')

    if p <= alpha:
        print('Reject Null, the monthly cash flow for suburban homes are greater than urban homes.')
    else:
        print('Cannot reject Null, the monthly cash flow for suburban homes are not significantly greater than urban homes.')


if __name__ == "__main__":

    suburbs_df = pd.read_csv('/home/jovyan/work/code/dsi/capstone-I/data/zillowQuerySuburb.csv')
    urban_denver_df = pd.read_csv('/home/jovyan/work/code/dsi/capstone-I/data/zillowQueryUrban.csv')
    ztest()

