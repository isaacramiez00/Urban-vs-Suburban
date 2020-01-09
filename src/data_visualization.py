import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import pandas as pd
import numpy as np
import folium


# I WAS WORKING HERE BUT NEED TO FINISH README
def plot_side_by_side_hist(suburban_df, urban_df):
    feature_columns = ['amount', 'rent', 'rentPerUnit', 'initialInvestment', 'monthlyCashFlow', 'oneYearNWROI']
    
    for i in feature_columns:
        fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True, figsize=(12,5))
        
        # # We can set the number of bins with the `bins` kwarg
        axs[0].hist(sub[i], color='red')
        axs[0].set_title(f'suburban {i}')
        axs[0].set_ylabel('count')
        axs[0].set_xlabel(f'{i}')
        suburb_mean = sub[i].mean()
        axs[0].axvline(x=sub[i].mean(), color='blue', label=f'mean {suburb_mean:.2f}')
        axs[0].legend(loc='best')

        # fig.subplots_adjust(wspace=0.4)

        axs[1].hist(urb[i], color='red')
        axs[1].set_title(f'urban {i}')
        axs[1].set_ylabel('count')
        axs[1].set_xlabel(f'{i}')
        urban_mean = urb[i].mean()
        axs[1].axvline(x=urb[i].mean(), color='blue', label=f'mean {urban_mean:.2f}')
        axs[1].legend(loc='best')
        
        plt.savefig(f'{i}_hist_urban_suburb.png')


def create_bar_charts(suburban, urban, col=['bedrooms', 'usecode'], x_labels=['Number of Bedrooms', 'Property Type']):


    for idx, i in enumerate(col):
        # bar chart of bedrooms
        before  = suburban[i].value_counts()
        after = urban[i].value_counts()
        bedrooms = pd.concat([before, after], axis=1)

        # udpated before/after var
        before = bedrooms.iloc[:,0].sort_values(ascending=False)
        after = bedrooms.iloc[:,1].sort_values(ascending=False)
    
        labels = before.index

        fig, ax = plt.subplots(figsize=(8,5))
        width = 0.4
        xlocs = np.arange(len(before))
        ax.bar(xlocs-width, before, width, label='Suburban', color='blue')
        ax.bar(xlocs, after, width, label='Urban', color='red')
        ax.set_xticks(ticks=range(len(before)))
        ax.set_xticklabels(labels)
        ax.yaxis.grid(True)
        ax.legend(loc='best')
        ax.set_ylabel('Mean Group result')
        ax.set_xlabel(x_labels[idx])
        ax.set_title(f'Number of {i} of Urban and suburban homes')
        fig.tight_layout(pad=1)
        plt.savefig(f'{i}_urban_suburban.png')


def denver_map():
    suburbs_df.sample(400)
    urban_denver_df.sample(400)

    denver_map = folium.Map(location=[39.73782,-104.971338],
                        zoom_start=10,
                        tiles="Cartodbpositron")
    locations = suburbs_df[['latitude', 'longitude']]
    locationlist = locations.values.tolist()
    urban_locations = urban_denver_df[['latitude', 'longitude']]
    urban_locationlist = urban_locations.values.tolist()

    for point in locationlist:
        folium.Circle(location=[point[0], point[1]], color='blue', radius=2).add_to(denver_map)
    for point in urban_locationlist:
        folium.Circle(location=[point[0], point[1]], color='red', radius=2).add_to(denver_map)

    return denver_map.save('folium_urban_suburban.html')


def cashflow_scatters(sub, urb, y_col, x_col='monthlyCashFlow' ):

    x1 = sub[x_col]
    y1 = sub[y_col]

    fig, ax = plt.subplots(2,1,figsize=(12,8))
    ax[0].scatter(x1,y1, alpha=0.5, color='orchid')
    ax[0].set_xlabel(x_col)
    ax[0].set_title(f'{x_col} over {y_col} for suburban homes')
    ax[0].set_ylabel(y_col)
    ax[0].grid(True)
    fig.tight_layout(pad=1)
    fig.subplots_adjust(hspace=0.6)


    x2 = urb[x_col]
    y2 = urb[y_col]
    ax[1].scatter(x2,y2, alpha=0.5, color='orchid')
    ax[1].set_xlabel(x_col)
    ax[1].set_title(f'{x_col} over {y_col} for urban homes')
    ax[1].set_ylabel(f'{y_col}')
    ax[1].grid(True)
    plt.savefig(f'{x_col}_over_{y_col}_suburbs_urban.png')
    



if __name__ == '__main__':

    # suburbs_df = pd.read_csv('/Users/isaacramirez/code/dsi/capstone-I/data/zillowQuerySuburb.csv')
    # urban_denver_df = pd.read_csv('/Users/isaacramirez/code/dsi/capstone-I/data/zillowQueryUrban.csv')

    suburbs_zillow_df = pd.read_csv('/home/jovyan/work/code/dsi/capstone-I/data/zillow_api/suburbanZillowQuery.csv')
    urban_denver_zillow_df = pd.read_csv('/home/jovyan/work/code/dsi/capstone-I/data/zillow_api/urbanZillowQuery.csv')

    # denver_map()
    # plot_histograms(suburbs_df, urban_denver_df)
    # create_bar_charts(suburbs_df, urban_denver_df)
    # y_col = ['amount', 'rent', 'rentPerUnit', 'initialInvestment', 'monthlyCashFlow', 'oneYearNWROI']

    # for y in y_col:
    #     cashflow_scatters(suburbs_df, urban_denver_df, y)


    
    