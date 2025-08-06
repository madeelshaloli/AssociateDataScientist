# FILTERING JOINS

# Merge employees and top_cust
empl_cust = employees.merge(top_cust, on='srid', 
                            how=left, indicator=True)

# Merge employees and top_cust
empl_cust = employees.merge(top_cust, on='srid', 
                                 how='left', indicator=True)

# Select the srid column where _merge is left_only
srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']

# Get employees not working with top customers
print(employees[employees['srid'].isin(srid_list)])

# Merge the non_mus_tcks and top_invoices tables on tid
tracks_invoices =non_mus_tcks.merge(top_invoices,on='tid')

# Use .isin() to subset non_mus_tcks to rows with tid in tracks_invoices
top_tracks = non_mus_tcks[non_mus_tcks['tid'].isin(tracks_invoices['tid'])]

# Group the top_tracks by gid and count the tid rows
cnt_by_gid = top_tracks.groupby(['gid'], as_index=False).agg({'tid':'count'})

# Merge the genres table to cnt_by_gid on gid and print
print(cnt_by_gid.merge(genres,on='gid'))


# Concatenate the tracks
tracks_from_albums = pd.concat([tracks_master,tracks_ride,tracks_st],
                               sort=True)
print(tracks_from_albums)


# Concatenate the tracks so the index goes from 0 to n-1
tracks_from_albums = pd.concat([tracks_master,tracks_ride,tracks_st],
                               ignore_index=True,
                               sort=True)
print(tracks_from_albums)


# Concatenate the tracks, show only columns names that are in all tables

tracks_from_albums = pd.concat([tracks_master,tracks_ride,tracks_st],
                        
                               sort=True,join='inner')
print(tracks_from_albums)


# Concatenate the tables and add keys
inv_jul_thr_sep = pd.concat([inv_jul,inv_aug,inv_sep], 
                            keys=['7Jul','8Aug','9Sep'])
print(inv_jul_thr_sep)
# Group the invoices by the index keys and find avg of the total column
avg_inv_by_month = inv_jul_thr_sep.groupby(level=0).agg({'total':'sum'})
print(avg_inv_by_month)

# Bar plot of avg_inv_by_month
avg_inv_by_month.plot(kind='bar')
plt.show()



# Concatenate the classic tables vertically
classic_18_19 = pd.concat([classic_18,classic_19],ignore_index=True)
print(classic_18_19)

# Concatenate the pop tables vertically
pop_18_19 = pd.concat([pop_18,pop_19],ignore_index=True)
print(pop_18_19)


# Concatenate the classic tables vertically
classic_18_19 = pd.concat([classic_18, classic_19], ignore_index=True)

# Concatenate the pop tables vertically
pop_18_19 = pd.concat([pop_18, pop_19], ignore_index=True)

# Merge classic_18_19 with pop_18_19
classic_pop = classic_18_19.merge(pop_18_19,on='tid')

# Using .isin(), filter classic_18_19 rows where tid is in classic_pop
popular_classic = classic_18_19[classic_18_19['tid'].isin(classic_pop['tid'])]

# Print popular chart
print(popular_classic)