
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
data_df = {'Name': ['Asha', 'Harsh', 'Sourav', 'Riya', 'Hritik',
                    'Shivansh', 'Rohan', 'Akash', 'Soumya', 'Kartik'],

           'Department': ['Administration', 'Marketing', 'Technical', 'Technical', 'Marketing',
                          'Administration', 'Technical', 'Marketing', 'Technical', 'Administration'],

           'Employment Type': ['Full-time Employee', 'Intern', 'Intern', 'Part-time Employee', 'Part-time Employee',
                               'Full-time Employee', 'Full-time Employee', 'Intern', 'Intern', 'Full-time Employee'],

           'Salary': [120000, 50000, 70000, 70000, 55000,
                      120000, 125000, 60000, 50000, 120000],

           'Years of Experience': [5, 1, 2, 3, 4,
                                   7, 6, 2, 1, 6]}


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
		number_to_gen = st.sidebar.number_input("Number",10,5000)
		localized_providers = ["ar_AA", "ar_EG", "ar_JO", "ar_PS", "ar_SA", "bg_BG", "bs_BA", "cs_CZ", "de", "de_AT", "de_CH", "de_DE", "dk_DK", "el_CY", "el_GR", "en", "en_AU", "en_CA", "en_GB", "en_IE", "en_IN", "en_NZ", "en_PH", "en_TH", "en_US", "es", "es_CA", "es_ES", "es_MX", "et_EE", "fa_IR", "fi_FI", "fil_PH", "fr_CA", "fr_CH", "fr_FR", "fr_QC", "he_IL", "hi_IN", "hr_HR", "hu_HU", "hy_AM", "id_ID", "it_CH", "it_IT", "ja_JP", "ka_GE", "ko_KR", "la", "lb_LU", "lt_LT", "lv_LV", "mt_MT", "ne_NP", "nl_BE", "nl_NL", "no_NO", "or_IN", "pl_PL", "pt_BR", "pt_PT", "ro_RO", "ru_RU", "sk_SK", "sl_SI", "sv_SE", "ta_IN", "th", "th_TH", "tl_PH", "tr_TR", "tw_GH", "uk_UA", "zh_CN", "zh_TW"]
		locale = st.sidebar.multiselect("Select Locale",localized_providers,default="en_US")
		dataformat = st.sidebar.selectbox("Save Data As",["csv","json"])

		df = generate_locale_profile(number_to_gen,locale)
		st.dataframe(df)
		with st.beta_expander("📩: Download"):
			make_downloadable_df_format(df,dataformat)

	elif choice == "Override Cust Life by Entity and EG":
		st.subheader("Override Cust Life by Entity and EG")
		# Locale Providers For Faker Class
		localized_providers = ["ar_AA", "ar_EG", "ar_JO", "ar_PS", "ar_SA", "bg_BG", "bs_BA", "cs_CZ", "de", "de_AT", "de_CH", "de_DE", "dk_DK", "el_CY", "el_GR", "en", "en_AU", "en_CA", "en_GB", "en_IE", "en_IN", "en_NZ", "en_PH", "en_TH", "en_US", "es", "es_CA", "es_ES", "es_MX", "et_EE", "fa_IR", "fi_FI", "fil_PH", "fr_CA", "fr_CH", "fr_FR", "fr_QC", "he_IL", "hi_IN", "hr_HR", "hu_HU", "hy_AM", "id_ID", "it_CH", "it_IT", "ja_JP", "ka_GE", "ko_KR", "la", "lb_LU", "lt_LT", "lv_LV", "mt_MT", "ne_NP", "nl_BE", "nl_NL", "no_NO", "or_IN", "pl_PL", "pt_BR", "pt_PT", "ro_RO", "ru_RU", "sk_SK", "sl_SI", "sv_SE", "ta_IN", "th", "th_TH", "tl_PH", "tr_TR", "tw_GH", "uk_UA", "zh_CN", "zh_TW"]
		locale = st.sidebar.multiselect("Select Locale",localized_providers,default="en_US")
		
		profile_options_list = ['username', 'name', 'sex' , 'address', 'mail' , 'birthdate''job', 'company', 'ssn', 'residence', 'current_location', 'blood_group', 'website'] 
		profile_fields = st.sidebar.multiselect("Fields",profile_options_list,default='username')

		number_to_gen = st.sidebar.number_input("Number",10,10000)
		dataformat = st.sidebar.selectbox("Save Data As",["csv","json"])

		# Initialize Faker Class
		custom_fake = Faker(locale)
		data = [custom_fake.profile(fields=profile_fields) for i in range(number_to_gen)]
		df = pd.DataFrame(data)

		# View As Dataframe
		st.dataframe(df)

		# View as JSON
		with st.beta_expander("🔍: View JSON "):
			st.json(data)

		with st.beta_expander("📩: Download"):
			make_downloadable_df_format(df,dataformat)
		

	else:
	       # Create the DataFrame
               df = pd.DataFrame(data_df)
               # Separate the rows into groups that have the same department
               groups = df.groupby('Department')

               # View the sum and the average of the numeric features of each group
               groups.aggregate(['mean', 'sum'])
               return df



if __name__ == '__main__':
	main()
