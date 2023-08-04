import streamlit as st
import pickle
import pandas as pd 
from sklearn.preprocessing import StandardScaler
from PIL import Image


with open('gridsearch.pkl', 'rb') as file:
    gridsearch = pickle.load(file)

RaptorFinal = pd.read_csv('raptorfinal.csv')

st.title('Hey Now Are You an Allstar')
image = Image.open('adj;lfkh;adsb.jpeg')
new_image = image.resize((600, 400))
st.image(new_image)


st.text('This application will help predict whether a player will be an allstar or not!')

st.header('Data was collected from NBA Player stats, All Star Selection Stats, and their Historical RAPTOR Scores')

st.header('Features will be included such as year, mpg, ppg, apg, etc.')

st.header('Time to train')

selected_year = st.sidebar.selectbox('season', RaptorFinal['season'].unique())
age = st.sidebar.slider('Age', int(RaptorFinal['age'].min()), int(RaptorFinal['age'].max()), int(RaptorFinal['age'].mean()))
g = st.sidebar.slider('Games Played', int(RaptorFinal['g'].min()), int(RaptorFinal['g'].max()), int(RaptorFinal['g'].mean()))
gs = st.sidebar.slider('Games Started', int(RaptorFinal['gs'].min()), int(RaptorFinal['gs'].max()), int(RaptorFinal['gs'].mean()))
mp_per_g = st.sidebar.slider('Minutes Per Game', float(RaptorFinal['mp_per_g'].min()), float(RaptorFinal['mp_per_g'].max()), float(RaptorFinal['mp_per_g'].mean()))
fg_per_g = st.sidebar.slider('Field Goals Per Game', float(RaptorFinal['fg_per_g'].min()), float(RaptorFinal['fg_per_g'].max()), float(RaptorFinal['fg_per_g'].mean()))
fga_per_g = st.sidebar.slider('Field Goals Attempted Per Game', float(RaptorFinal['fga_per_g'].min()), float(RaptorFinal['fga_per_g'].max()), float(RaptorFinal['fga_per_g'].mean()))
fg_pct = st.sidebar.slider('Field Goal Percentage', float(RaptorFinal['fg_pct'].min()), float(RaptorFinal['fg_pct'].max()), float(RaptorFinal['fg_pct'].mean()))
fg3_per_g = st.sidebar.slider('Three-Point Field Goals Per Game', float(RaptorFinal['fg3_per_g'].min()), float(RaptorFinal['fg3_per_g'].max()), float(RaptorFinal['fg3_per_g'].mean()))
fg3a_per_g = st.sidebar.slider('Three-Point Field Goals Attempted Per Game', float(RaptorFinal['fg3a_per_g'].min()), float(RaptorFinal['fg3a_per_g'].max()), float(RaptorFinal['fg3a_per_g'].mean()))
fg3_pct = st.sidebar.slider('Three-Point Field Goal Percentage', float(RaptorFinal['fg3_pct'].min()), float(RaptorFinal['fg3_pct'].max()), float(RaptorFinal['fg3_pct'].mean()))
fg2_per_g = st.sidebar.slider('Two-Point Field Goals Per Game', float(RaptorFinal['fg2_per_g'].min()), float(RaptorFinal['fg2_per_g'].max()), float(RaptorFinal['fg2_per_g'].mean()))
fg2a_per_g = st.sidebar.slider('Two-Point Field Goals Attempted Per Game', float(RaptorFinal['fg2a_per_g'].min()), float(RaptorFinal['fg2a_per_g'].max()), float(RaptorFinal['fg2a_per_g'].mean()))
fg2_pct = st.sidebar.slider('Two-Point Field Goal Percentage', float(RaptorFinal['fg2_pct'].min()), float(RaptorFinal['fg2_pct'].max()), float(RaptorFinal['fg2_pct'].mean()))
efg_pct = st.sidebar.slider('Effective Field Goal Percentage', float(RaptorFinal['efg_pct'].min()), float(RaptorFinal['efg_pct'].max()), float(RaptorFinal['efg_pct'].mean()))
ft_per_g = st.sidebar.slider('Free Throws Per Game', float(RaptorFinal['ft_per_g'].min()), float(RaptorFinal['ft_per_g'].max()), float(RaptorFinal['ft_per_g'].mean()))
fta_per_g = st.sidebar.slider('Free Throws Attempted Per Game', float(RaptorFinal['fta_per_g'].min()), float(RaptorFinal['fta_per_g'].max()), float(RaptorFinal['fta_per_g'].mean()))
ft_pct = st.sidebar.slider('Free Throw Percentage', float(RaptorFinal['ft_pct'].min()), float(RaptorFinal['ft_pct'].max()), float(RaptorFinal['ft_pct'].mean()))
orb_per_g = st.sidebar.slider('Offensive Rebounds Per Game', float(RaptorFinal['orb_per_g'].min()), float(RaptorFinal['orb_per_g'].max()), float(RaptorFinal['orb_per_g'].mean()))
drb_per_g = st.sidebar.slider('Defensive Rebounds Per Game', float(RaptorFinal['drb_per_g'].min()), float(RaptorFinal['drb_per_g'].max()), float(RaptorFinal['drb_per_g'].mean()))
trb_per_g = st.sidebar.slider('Total Rebounds Per Game', float(RaptorFinal['trb_per_g'].min()), float(RaptorFinal['trb_per_g'].max()), float(RaptorFinal['trb_per_g'].mean()))
ast_per_g = st.sidebar.slider('Assists Per Game', float(RaptorFinal['ast_per_g'].min()), float(RaptorFinal['ast_per_g'].max()), float(RaptorFinal['ast_per_g'].mean()))
stl_per_g = st.sidebar.slider('Steals Per Game', float(RaptorFinal['stl_per_g'].min()), float(RaptorFinal['stl_per_g'].max()), float(RaptorFinal['stl_per_g'].mean()))
blk_per_g = st.sidebar.slider('Blocks Per Game', float(RaptorFinal['blk_per_g'].min()), float(RaptorFinal['blk_per_g'].max()), float(RaptorFinal['blk_per_g'].mean()))
tov_per_g = st.sidebar.slider('Turnovers Per Game', float(RaptorFinal['tov_per_g'].min()), float(RaptorFinal['tov_per_g'].max()), float(RaptorFinal['tov_per_g'].mean()))
pf_per_g = st.sidebar.slider('Personal Fouls Per Game', float(RaptorFinal['pf_per_g'].min()), float(RaptorFinal['pf_per_g'].max()), float(RaptorFinal['pf_per_g'].mean()))
pts_per_g = st.sidebar.slider('Points Per Game', float(RaptorFinal['pts_per_g'].min()), float(RaptorFinal['pts_per_g'].max()), float(RaptorFinal['pts_per_g'].mean()))
mp = st.sidebar.slider('Minutes Played', float(RaptorFinal['mp'].min()), float(RaptorFinal['mp'].max()), float(RaptorFinal['mp'].mean()))
per = st.sidebar.slider('Player Efficiency Rating (PER)', float(RaptorFinal['per'].min()), float(RaptorFinal['per'].max()), float(RaptorFinal['per'].mean()))
ts_pct = st.sidebar.slider('True Shooting Percentage', float(RaptorFinal['ts_pct'].min()), float(RaptorFinal['ts_pct'].max()), float(RaptorFinal['ts_pct'].mean()))
fg3a_per_fga_pct = st.sidebar.slider('Three-Point Attempt Rate', float(RaptorFinal['fg3a_per_fga_pct'].min()), float(RaptorFinal['fg3a_per_fga_pct'].max()), float(RaptorFinal['fg3a_per_fga_pct'].mean()))
fta_per_fga_pct = st.sidebar.slider('Free Throw Attempt Rate', float(RaptorFinal['fta_per_fga_pct'].min()), float(RaptorFinal['fta_per_fga_pct'].max()), float(RaptorFinal['fta_per_fga_pct'].mean()))
orb_pct = st.sidebar.slider('Offensive Rebound Percentage', float(RaptorFinal['orb_pct'].min()), float(RaptorFinal['orb_pct'].max()), float(RaptorFinal['orb_pct'].mean()))
drb_pct = st.sidebar.slider('Defensive Rebound Percentage', float(RaptorFinal['drb_pct'].min()), float(RaptorFinal['drb_pct'].max()), float(RaptorFinal['drb_pct'].mean()))
trb_pct = st.sidebar.slider('Total Rebound Percentage', float(RaptorFinal['trb_pct'].min()), float(RaptorFinal['trb_pct'].max()), float(RaptorFinal['trb_pct'].mean()))
ast_pct = st.sidebar.slider('Assist Percentage', float(RaptorFinal['ast_pct'].min()), float(RaptorFinal['ast_pct'].max()), float(RaptorFinal['ast_pct'].mean()))
stl_pct = st.sidebar.slider('Steal Percentage', float(RaptorFinal['stl_pct'].min()), float(RaptorFinal['stl_pct'].max()), float(RaptorFinal['stl_pct'].mean()))
blk_pct = st.sidebar.slider('Block Percentage', float(RaptorFinal['blk_pct'].min()), float(RaptorFinal['blk_pct'].max()), float(RaptorFinal['blk_pct'].mean()))
tov_pct = st.sidebar.slider('Turnover Percentage', float(RaptorFinal['tov_pct'].min()), float(RaptorFinal['tov_pct'].max()), float(RaptorFinal['tov_pct'].mean()))
usg_pct = st.sidebar.slider('Usage Percentage', float(RaptorFinal['usg_pct'].min()), float(RaptorFinal['usg_pct'].max()), float(RaptorFinal['usg_pct'].mean()))
ows = st.sidebar.slider('Offensive Win Shares', float(RaptorFinal['ows'].min()), float(RaptorFinal['ows'].max()), float(RaptorFinal['ows'].mean()))
dws = st.sidebar.slider('Defensive Win Shares', float(RaptorFinal['dws'].min()), float(RaptorFinal['dws'].max()), float(RaptorFinal['dws'].mean()))
ws = st.sidebar.slider('Win Shares', float(RaptorFinal['ws'].min()), float(RaptorFinal['ws'].max()), float(RaptorFinal['ws'].mean()))
ws_per_48 = st.sidebar.slider('Win Shares Per 48 Minutes', float(RaptorFinal['ws_per_48'].min()), float(RaptorFinal['ws_per_48'].max()), float(RaptorFinal['ws_per_48'].mean()))
obpm = st.sidebar.slider('Offensive Box Plus/Minus', float(RaptorFinal['obpm'].min()), float(RaptorFinal['obpm'].max()), float(RaptorFinal['obpm'].mean()))
dbpm = st.sidebar.slider('Defensive Box Plus/Minus', float(RaptorFinal['dbpm'].min()), float(RaptorFinal['dbpm'].max()), float(RaptorFinal['dbpm'].mean()))
bpm = st.sidebar.slider('Box Plus/Minus', float(RaptorFinal['bpm'].min()), float(RaptorFinal['bpm'].max()), float(RaptorFinal['bpm'].mean()))
vorp = st.sidebar.slider('Value Over Replacement Player', float(RaptorFinal['vorp'].min()), float(RaptorFinal['vorp'].max()), float(RaptorFinal['vorp'].mean()))
award_share = st.sidebar.slider('Award Share', float(RaptorFinal['award_share'].min()), float(RaptorFinal['award_share'].max()), float(RaptorFinal['award_share'].mean()))
mov = st.sidebar.slider('Margin of Victory', float(RaptorFinal['mov'].min()), float(RaptorFinal['mov'].max()), float(RaptorFinal['mov'].mean()))
mov_adj = st.sidebar.slider('Margin of Victory (Adjusted)', float(RaptorFinal['mov_adj'].min()), float(RaptorFinal['mov_adj'].max()), float(RaptorFinal['mov_adj'].mean()))
win_loss_pct = st.sidebar.slider('Team Win-Loss Percentage', float(RaptorFinal['win_loss_pct'].min()), float(RaptorFinal['win_loss_pct'].max()), float(RaptorFinal['win_loss_pct'].mean()))
raptor_offense = st.sidebar.slider('Raptor Offense', float(RaptorFinal['raptor_offense'].min()), float(RaptorFinal['raptor_offense'].max()), float(RaptorFinal['raptor_offense'].mean()))
raptor_defense = st.sidebar.slider('Raptor Defense', float(RaptorFinal['raptor_defense'].min()), float(RaptorFinal['raptor_defense'].max()), float(RaptorFinal['raptor_defense'].mean()))
raptor_total = st.sidebar.slider('Raptor Total', float(RaptorFinal['raptor_total'].min()), float(RaptorFinal['raptor_total'].max()), float(RaptorFinal['raptor_total'].mean()))




new_data = {
    'season': selected_year,
    'age': age,
    'g': g,
    'gs': gs,
    'mp_per_g': mp_per_g,
    'fg_per_g': fg_per_g,
    'fga_per_g': fga_per_g,
    'fg_pct': fg_pct,
    'fg3_per_g': fg3_per_g,
    'fg3a_per_g': fg3a_per_g,
    'fg3_pct': fg3_pct,
    'fg2_per_g': fg2_per_g,
    'fg2a_per_g': fg2a_per_g,
    'fg2_pct': fg2_pct,
    'efg_pct': efg_pct,
    'ft_per_g': ft_per_g,
    'fta_per_g': fta_per_g,
    'ft_pct': ft_pct,
    'orb_per_g': orb_per_g,
    'drb_per_g': drb_per_g,
    'trb_per_g': trb_per_g,
    'ast_per_g': ast_per_g,
    'stl_per_g': stl_per_g,
    'blk_per_g': blk_per_g,
    'tov_per_g': tov_per_g,
    'pf_per_g': pf_per_g,
    'pts_per_g': pts_per_g,
    'mp': mp,
    'per': per,
    'ts_pct': ts_pct,
    'fg3a_per_fga_pct': fg3a_per_fga_pct,
    'fta_per_fga_pct': fta_per_fga_pct,
    'orb_pct': orb_pct,
    'drb_pct': drb_pct,
    'trb_pct': trb_pct,
    'ast_pct': ast_pct,
    'stl_pct':stl_pct,
    'blk_pct': blk_pct,
    'tov_pct': tov_pct,
    'usg_pct': usg_pct,
    'ows': ows,
    'dws': dws,
    'ws': ws,
    'ws_per_48': ws_per_48,
    'obpm': obpm,
    'dbpm': dbpm,
    'bpm': bpm,
    'vorp': vorp,
    'award_share': award_share,
    'mov': mov,
    'mov_adj': mov_adj,
    'win_loss_pct': win_loss_pct,
    'Year' : selected_year,
    'raptor_offense': raptor_offense,
    'raptor_defense': raptor_defense,
    'raptor_total': raptor_total
}

st.write(new_data)

z = pd.Series(new_data)

pred_array = z.to_frame().T

fit_cols = ['season', 'age', 'g', 'gs', 'mp_per_g', 'fg_per_g', 'fga_per_g',
       'fg_pct', 'fg3_per_g', 'fg3a_per_g', 'fg3_pct', 'fg2_per_g',
       'fg2a_per_g', 'fg2_pct', 'efg_pct', 'ft_per_g', 'fta_per_g', 'ft_pct',
       'orb_per_g', 'drb_per_g', 'trb_per_g', 'ast_per_g', 'stl_per_g',
       'blk_per_g', 'tov_per_g', 'pf_per_g', 'pts_per_g', 'mp', 'per',
       'ts_pct', 'fg3a_per_fga_pct', 'fta_per_fga_pct', 'orb_pct', 'drb_pct',
       'trb_pct', 'ast_pct', 'stl_pct', 'blk_pct', 'tov_pct', 'usg_pct', 'ows',
       'dws', 'ws', 'ws_per_48', 'obpm', 'dbpm', 'bpm', 'vorp', 'award_share',
       'mov', 'mov_adj', 'win_loss_pct', 'raptor_offense',
       'raptor_defense', 'raptor_total']

ss = StandardScaler()

RaptorFinal.drop(columns = ['Unnamed: 0'], inplace = True)
ss.fit(RaptorFinal.select_dtypes('number'))
pred_array =ss.transform(pred_array)




if st.button('predict!'):

    pred = gridsearch.predict(pred_array)

    st.write(pred)

    if pred == 1: 
        st.write('all star yo')
    else: 
        st.write('dude sucks')
