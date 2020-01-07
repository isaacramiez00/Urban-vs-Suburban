import matplotlib.pyplot as plt

def plot_histograms(sub, urb, col=col):
    col = ['amount', 'rent', 'rentPerUnit', 'initialInvestment', 'monthlyCashFlow', 'oneYearNWROI']
    
    
    for i in col:
        
        fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)
        
        # # We can set the number of bins with the `bins` kwarg
        axs[0].hist(sub[i])
        axs[0].set_title(f'suburban {i}')
        axs[0].set_ylabel('count')
        suburb_mean = sub[i].mean()
        axs[0].axvline(x=sub[i].mean(), color='blue', label=f'mean {suburb_mean:.2f}')
        axs[0].legend(loc='best')


        axs[1].hist(urb[i])
        axs[1].set_title(f'urban {i}')
        axs[1].set_ylabel('count')
        urban_mean = urb[i].mean()
        axs[1].axvline(x=urb[i].mean(), color='blue', label=f'mean {urban_mean:.2f}')
        axs[1].legend(loc='best')
        
        plt.savefig(f'{i}_hist_urban_suburb.png')


def bedroom_bar_chart():
    before = suburbs_df['bedrooms']
    after = urban_denver_df['bedrooms']

    fig, ax = plt.subplots(figsize=(8,5))
    width = 0.4
    xlocs = np.arange(len(before))
    ax.bar(xlocs-width, before, width, label='Suburban')
    ax.bar(xlocs, after, width, label='Urban')

    # bar chart of bedrooms
    before  = suburbs_df['bedrooms'].value_counts()
    after = urban_denver_df['bedrooms'].value_counts()
    bedrooms = pd.concat([before, after], axis=1)

    # udpated before/after var
    before = bedrooms.iloc[:,0]
    after = bedrooms.iloc[:,1]

    ax.set_xticks(ticks=range(len(before)))
    ax.yaxis.grid(True)

    before = bedrooms.iloc[:,0]
    after = bedrooms.iloc[:,1]
    labels = bedrooms.index

    fig, ax = plt.subplots(figsize=(8,5))
    width = 0.4
    xlocs = np.arange(len(before))
    ax.bar(xlocs-width, before, width, label='Suburban')
    ax.bar(xlocs, after, width, label='Urban')
    ax.set_xticks(ticks=range(len(before)))
    ax.set_xticklabels(labels)
    ax.yaxis.grid(True)
    ax.legend(loc='best')
    ax.set_ylabel('Mean Group result')
    ax.set_title('Number of bedrooms of Urban and suburban homes')
    fig.tight_layout(pad=1)
    plt.savefig('bedroom_urban_suburban.png')

def denver_map():
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
