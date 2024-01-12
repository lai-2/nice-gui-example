import os

from nicegui import ui

true, false, none = True, False, None

# ---------------------------------------------

WIPO_STYLES = '''
<style>
body {
	font-size : 20px ;
}
img[src$="pdf.svg"] ,
img[src$="zip.svg"] {
    background-image: initial;
    background-color: rgb(0, 77, 169);
	display : inline-block ;
    background: #0067B8;
    padding: 3px;
    max-height: 16px;
    /* vertical-align: text-bottom; */
    margin: 0 4px;
}

a {
    color: #0059C6 !important;
}

p
{
	margin-bottom : 1em !important ;
}

h1, h2, h3, h4, h5, h6 ,
/* .text-h1, .text-h2, .text-h3, */
.text-h4, .text-h5, .text-h6
{
	margin-top : 1em !important ;
	margin-bottom : 0.5em !important ;
}
</style>
'''

# ---------------------------------------------

async def alert () :
	await ui.run_javascript ('alert("Hello!")', respond = false)

# ---------------------------------------------

ISDARK = true

#@ui.page ('/')
def mainpage () :

	ui.add_head_html (WIPO_STYLES)

	# adding wipo stylesheets breaks the page
	#ui.add_head_html ('<link rel="https://www.wipo.int/stylesheet" href="https://www.wipo.int/export/system/modules/org.wipo.internet.rwd.templates/resources/css/styles2016.css">')
	#ui.add_head_html ('<link rel="https://www.wipo.int/stylesheet" href="https://www.wipo.int/export/system/modules/org.wipo.internet.rwd.templates/resources/css/styles2016-universal.css">')
	#ui.add_head_html ('<link rel="https://www.wipo.int/stylesheet" href="https://www.wipo.int/export/system/modules/org.wipo.internet.rwd.templates/resources/webfonts/ss-standard.css">')


	dark = ui.dark_mode ()

	# -----

	with ui.left_drawer (top_corner = true, bottom_corner = true).style ('background-color: #33c'):

		switch = ui.switch ('Dark mode', value = ISDARK, on_change = dark.toggle)

		#ui.label ('Switch mode:')
		#ui.button ('Dark', on_click = dark.enable)
		#ui.button ('Light', on_click = dark.disable)

	# -----

	ui.label ('WIPO Sequence').classes ('text-h3')

	with ui.element ('div').classes ('') :
		ui.image ('https://www.wipo.int/export/sites/www/standards/images/wipo-sequence-845.jpg').props ('width=25vw').style ('margin-bottom:2em; margin-left:3em').classes ('float-right')

		ui.html ('''
<p>WIPO Sequence is a global software tool that enables patent applicants to prepare amino acid and nucleotide sequence listings compliant with <a href="https://www.wipo.int//export/sites/www/standards/en/pdf/03-26-01.pdf" rel="https://www.wipo.int/noopener">WIPO Standard ST.26 <img src="https://www.wipo.int//export/sites/www/shared/images/icon/new/pdf.svg" alt="PDF, WIPO Standard ST.26"></a> as part of a national or international patent application.</p>

<p class="lead">WIPO Sequence Validator is a web service for patent offices to verify that filed sequence listings comply with WIPO ST.26.</p>

<p>These tools were developed in collaboration with patent offices around the world, under the direction of the <a href="https://www.wipo.int//cws/en/">Committee on WIPO Standards</a>.</p>

<div class="alert alert--warning">
<p><strong>Note</strong>: WIPO Standard ST.26 is now in force.</p>
<p>WIPO Sequence Suite version 2.3.0 was released on 2023.05.08</p>
</div>
		''')

	ui.separator ()

	# -----

	with ui.tabs ().classes ('w-full') as tabs :
		tabapp = ui.tab ('For Applicants')
		taboff = ui.tab ('For Patent Offices')

	with ui.tab_panels (tabs, value = tabapp).classes ('w-50') :

		with ui.tab_panel (tabapp) :

			ui.label ('WIPO Sequence Suite').classes ('text-h4')

			ui.html ('''
<p>A standalone desktop application available for Windows, Linux and MacOS. A <a href="https://www.wipo.int/export/sites/www/standards/en/sequence/wipo-sequence-manual.pdf">User Manual <img src="https://www.wipo.int/export/sites/www/shared/images/icon/new/pdf.svg" alt="PDF, WIPO Sequence version 1.1.0 User Manual"></a> is provided to assist applicants with generating compliant sequence listings.</p>
			''')

			with ui.card ().classes ('bg-stone-200 dark:bg-stone-700 w-50 float-right') :
				
				with ui.element ('div').classes ('text-h6 w-full') :
					ui.icon ('help').classes ('float-left')
					ui.label ('Need help?')

				ui.html ('''
<p>Visit the Knowledge Base for help with WIPO Sequence.</p>
<p>This includes known issues and how to report bugs.</p>
				''')

				ui.button (
					'Knowledge Base',
					icon = 'rocket' ,
					on_click = 'https://www3.wipo.int/confluence/x/EwAxRg' ,
				).classes ('bg-blue-700')

			ui.label ('Download').classes ('text-h6')
			ui.html ( '''
<p>By downloading and installing WIPO Sequence, you are accepting the following <a href="https://www.wipo.int/export/sites/www/standards/en/sequence/wipo-sequence-terms-use-en.pdf">Terms of Use (October 2021) </a>.</p>
			''')

			# ---

			ui.label ('Select your platform...')

			def startdl (link) :
				ui.download (link)
				ui.notify('Your download has started', type = 'positive')

			dlwin = 'https://wiposequence.wipo.int/download/wiposequence/win/WIPO+Sequence+Setup+2.3.0.exe'
			dlmac = 'https://wiposequence.wipo.int/download/wiposequence/osx/WIPO Sequence-2.3.0.dmg'
			dlnix = 'https://wiposequence.wipo.int/download/wiposequence/linux/WIPO%20Sequence%202.3.0.AppImage'

			dlc = 'bg-green-400 dark:bg-green-600'
			cls = dlc + ' block m-4'

			ui.button ('Mac OS' , icon = 'favorite' , on_click = lambda : startdl (dlmac), color = dlc).classes (cls)
			ui.button ('Linux'  , icon = 'plumbing' , on_click = lambda : startdl (dlnix), color = dlc).classes (cls)
			ui.button ('Windows', icon = 'delete' , on_click = lambda : startdl (dlwin), color = dlc).classes (cls)

			# ---

			ui.label ('Updates').classes ('text-h6')
			ui.html ('''
<p>Sign up for the mailing list to receive notifications of software updates and related issues: <a id="signup" href="/standards/en/sequence/signup.html">WIPO Sequence Updates</a></p>
			''')

			ui.label ('Test data set — ST.26 DTD version 1.3').classes ('text-h6')
			ui.html ('''
<p>The following ZIP file provides both compliant and non-compliant ST.26 instances for testing purposes: Test data set <a href="https://www.wipo.int/standards/en/sequence/valid_and_error.zip"><img src="https://www.wipo.int/export/sites/www/shared/images/icon/new/zip.svg" alt="ZIP, Test data set ST.26 DTD version 1.3"></a></p>
			''')

		# ---

		with ui.tab_panel (taboff) :

			ui.label ('WIPO Sequence Validator').classes ('text-h4')

			ui.html ('''
<p>A web service that runs in patent office environments to check filed sequence listings for compliance with WIPO Standard ST.26. Patent Offices may obtain WIPO Sequence Validator by <a href="mailto:wiposequence@wipo.int">contacting us</a>.</p>
<h3>Validator Materials</h3>
<ul>
<li><a href="/export/sites/www/standards/en/sequence/wipo-sequence-validator-terms-use-en.pdf" rel="noopener">WIPO Sequence Validator Terms of Use <img src="https://www.wipo.int/export/sites/www/shared/images/icon/new/pdf.svg" alt="PDF, WIPO Sequence Validator Terms of Use"></a></li>
<li><a href="/export/sites/www/standards/en/sequence/wipo-sequence-validator-manual-2-3-0.pdf">WIPO Sequence Validator Operations Manual <img src="https://www.wipo.int/export/sites/www/shared/images/icon/new/pdf.svg" alt="PDF, WIPO Sequence Validator version 1.1.0 Operations Manual"></a></li>
</ul>
			''')

			ui.separator()

	# -----

	ui.label ('News').classes ('text-h4') 

	with ui.timeline (side = 'right') :
		
		ui.timeline_entry (
			'' ,
			title    = 'Version 2.2.0 of WIPO Sequence Suite released for general use' ,
			subtitle = 'Oct 2022' ,
			icon     = 'rocket_launch' ,
		)

		with ui.timeline_entry (
			'' ,
			title    = 'WIPO Standard ST.26 goes live' ,
			subtitle = 'July 2022' ,
			icon     = 'biotech' ,
		) :
			
			ui.link ('Full story ', 'https://www.wipo.int/pct/en/news/2022/news_0039.html', new_tab = true)
			ui.icon ('launch')

		with ui.timeline_entry (
			'' ,
			title    = 'Version 2.1 of WIPO Sequence Suite released ' ,
			subtitle = 'June 2022' ,
			icon     = 'public' ,
		) :
			with ui.expansion ('Show more', icon = 'swap_vert').classes ('w-full') :
				ui.html ('''
<p>After releasing WIPO Sequence Suite version 2.0 in May, WIPO has continued resolving known issues to ensure the software is production ready for the WIPO ST.26 implementation date of July 1. Improvements in version 2.1 include upgrading the “Help” features and refining import messages. Changes since version 2.0.0 are summarized in the Release Notes on the <a href="https://www.wipo.int/standards/en/sequence/index.html">WIPO Sequence home page</a>.</p>
<p>If you do not receive the auto-update message in WIPO Sequence Suite, please download version 2.1.0 using the links above.</p>
				''')

		with ui.timeline_entry (
			'' ,
			title    = 'Next stable release of WIPO Sequence; Knowledge Base & email list' ,
			subtitle = 'May 2022' ,
			icon     = 'model_training' ,
		) :

			with ui.expansion ('Show more', icon = 'swap_vert').classes ('w-full') :
				ui.html ('''
<p>Based on the feedback of our testing group, WIPO has continued to improve the WIPO Sequence Suite to ensure that it meets the needs of users for the July 1 WIPO ST.26 implementation date. The result will be WIPO Sequence version 2.0.0, scheduled for release in the week of May 16. Improvements since the last stable version will be summarized in the Version 2.0.0 Release Notes to be provided in the Download section.</p>
<p>To help support users, WIPO is also collaborating with patent Offices to produce a <a href="https://www3.wipo.int/confluence/x/EwAxRg">knowledge base</a> of answers to regularly asked questions and common issues. This knowledge base will be available to the public from June 1.</p>
<p>WIPO Sequence users are encouraged to sign-up to the new <a href="/standards/en/sequence/signup.html">email list</a> for important announcements and information on software updates and related issues. Users will be prompted to register for the list when downloading the software from the WIPO Sequence homepage. </p>
</article>
				''')

		with ui.timeline_entry (
			'' ,
			title    = 'Second stable release of WIPO Sequence' ,
			subtitle = 'Oct 2021' ,
			icon     = 'build' ,
		) :

			with ui.expansion ('Show more', icon = 'swap_vert').classes ('w-full') :
				ui.html ('''
<p>Since November 2021, WIPO has been developing an improved version of the WIPO Sequence Suite. The latest version of the desktop tool can be downloaded above along with the release notes which indicate the changes since the last stable release was published. Patent Offices interested in the latest version of WIPO Sequence Validator should <a href="mailto:wiposequence@wipo.int">contact us</a>.</p>
				''')

		with ui.timeline_entry (
			'' ,
			title    = 'WIPO ST.26 Training Webinar Series' ,
			subtitle = 'April 2021' ,
			icon     = 'ondemand_video' ,
		) :
			
			with ui.expansion ('Show more', icon = 'swap_vert').classes ('w-full') :
				ui.html ('''
<p>WIPO is providing four webinars on preparing sequence listings compliant with WIPO Standard ST.26. The webinars are open to patent applicants and IP Offices. See the <a href="https://www.wipo.int/meetings/en/topic.jsp?group_id=330">webinars page</a> for dates in April and May and other information. Recordings will be available.</p>
				''')

	ui.separator()
	
	title = 'WIPO Sequence'

	if ISDARK :
		dark.enable ()

	ui.run (
		title = title ,
#		dark = true ,  # doesnt work
#		port = native_mode.find_open_port () ,
#		reload = false,
	)

# ---------------------------------------------

if __name__ in { '__main__', '__mp_main__' } :
	mainpage ()
