# Core Pkgs
import streamlit as st 
import streamlit.components.v1 as stc 

# Data Pkgs
import pandas as pd 
from faker import Faker


# Utils
import base64
import time 
timestr = time.strftime("%Y%m%d-%H%M%S")


# Fxn to Download
def make_downloadable_df(data):
    csvfile = data.to_csv(index=False)
    b64 = base64.b64encode(csvfile.encode()).decode()  # B64 encoding
    st.markdown("### ** Download CSV File ** ")
    new_filename = "fake_dataset_{}.csv".format(timestr)
    href = f'<a href="data:file/csv;base64,{b64}" download="{new_filename}">Click Here!</a>'
    st.markdown(href, unsafe_allow_html=True)

# Fxn to Download Into A Format
def make_downloadable_df_format(data,format_type="csv"):
	if format_type == "csv":
		datafile = data.to_csv(index=False)
	elif format_type == "json":
		datafile = data.to_json()
	b64 = base64.b64encode(datafile.encode()).decode()  # B64 encoding
	st.markdown("### ** Download File  📩 ** ")
	new_filename = "fake_dataset_{}.{}".format(timestr,format_type)
	href = f'<a href="data:file/{format_type};base64,{b64}" download="{new_filename}">Click Here!</a>'
	st.markdown(href, unsafe_allow_html=True)


# Generate A Simple Profile
def generate_profile(number,random_seed=200):
	fake = Faker()
	Faker.seed(random_seed)
	data = [fake.simple_profile() for i in range(number)]
	df = pd.DataFrame(data)
	return df 

# Generate A Customized Profile Per Locality
def generate_locale_profile(number,locale,random_seed=200):
	locale_fake = Faker(locale)
	Faker.seed(random_seed)
	data = [locale_fake.simple_profile() for i in range(number)]
	df = pd.DataFrame(data)
	return df 


custom_title = """
<div style="font-size:40px;font-weight:bolder;background-color:#fff;padding:10px;
border-radius:10px;border:5px solid #464e5f;text-align:center;">
		<span style='color:blue'>C</span>
		<span style='color:black'>a</span>
		<span style='color:black'>p</span>
		<span style='color:black'>i</span>
		<span style='color:black'>t</span>
		<span style='color:black'>a</span>
		<span style='color:black'>l</span>
		<span style='color:blue'>C</span>
		<span style='color:black'>o</span>
		<span style='color:black'>m</span>
		<span style='color:black'>m</span>
		<span style='color:black'>i</span>
		<span style='color:black'>s</span>
		<span style='color:black'>s</span>
		<span style='color:black'>i</span>
		<span style='color:black'>o</span>
		<span style='color:black'>n</span>
		<span style='color:blue'>A</span>
		<span style='color:black'>p</span>
		<span style='color:black'>p</span>
		
</div>
"""


def main():
	# st.title("Capital Commission App")
	stc.html(custom_title)

	webforms = ["Expense Category and Cust Life by EG","Override Cust Life by Entity and EG","Record Classification and Catchup Month by Role"]

	choice = st.sidebar.selectbox("Webforms",webforms)
	if choice == "Expense Category and Cust Life by EG":
		st.subheader("Expense Category and Cust Life by EG")
		dataformat = st.sidebar.selectbox("Fiscal Year",["2021","2022"])
		
		dataformat = st.sidebar.selectbox("Save Data As",["csv","json"])
		

		multi_index = pd.MultiIndex.from_tuples([("1","EG_RENEWALS_EARNINGS"),
                                       ("2","EG_RENEWAL_RATE"),("3","EG_RENEWALS_ADVANCE")],
                                       names=['Courses','Fee'])
		
		cols = pd.MultiIndex.from_tuples([("April", "CapVsExp"), 
                                  ("April", "EG_Customer_Life"), 
                                  ("May", "CapVsExp"),
                                  ("May", "EG_Customer_Life")])
		
		

		df = pd.DataFrame(columns=cols,index=multi_index)




		
		
		st.dataframe(df)
		with st.beta_expander("📩: Download"):
			make_downloadable_df_format(df,dataformat)

	elif choice == "Override Cust Life by Entity and EG":
		st.subheader("Override Cust Life by Entity and EG")
		dataformat = st.sidebar.selectbox("Entity",["E_500","E_600"])
		dataformat = st.sidebar.selectbox("Save Data As",["csv","json"])

		
		# View As Dataframe
		multi_index = pd.MultiIndex.from_tuples([("1","EG_RENEWALS_EARNINGS"),
                                       ("2","EG_RENEWAL_RATE"),("3","EG_RENEWALS_ADVANCE")],
                                       names=['Courses','Fee'])
		
		cols = pd.MultiIndex.from_tuples([("April", "CapVsExp"), 
                                  ("April", "EG_Customer_Life"), 
                                  ("May", "CapVsExp"),
                                  ("May", "EG_Customer_Life")])
		
		

		df = pd.DataFrame(columns=cols,index=multi_index)
		st.dataframe(df)

		

		with st.beta_expander("📩: Download"):
			make_downloadable_df_format(df,dataformat)
		

	elif choice == "Record Classification and Catchup Month by Role":
		st.subheader("Record Classification and Catchup Month by Role")
		dataformat = st.sidebar.selectbox("Entity",["E_500","E_600"])
		dataformat = st.sidebar.selectbox("Save Data As",["csv","json"])

		
		# View As Dataframe
		multi_index = pd.MultiIndex.from_tuples([("1","EG_RENEWALS_EARNINGS"),
                                       ("2","EG_RENEWAL_RATE"),("3","EG_RENEWALS_ADVANCE")],
                                       names=['Courses','Fee'])
		
		cols = pd.MultiIndex.from_tuples([("April", "CapVsExp"), 
                                  ("April", "EG_Customer_Life"), 
                                  ("May", "CapVsExp"),
                                  ("May", "EG_Customer_Life")])
		
		

		df = pd.DataFrame(columns=cols,index=multi_index)
		st.dataframe(df)

		# View as JSON
		with st.beta_expander("🔍: View JSON "):
			st.json(data)

		with st.beta_expander("📩: Download"):
			make_downloadable_df_format(df,dataformat)
		
		







if __name__ == '__main__':
	main()
