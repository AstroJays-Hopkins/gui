import matplotlib.pyplot as plt
# import cartopy.crs as ccrs

ax1 = plt.subplot(311)
ax2 = plt.subplot(312, projection='polar')


print(type(ax1))
print(type(ax2))

plt.show()