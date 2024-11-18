ProgressBarWindowTemplate = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>ProgressBarWindow</class>
 <widget class="QSplashScreen" name="ProgressBarWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>710</width>
    <height>370</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>710</width>
    <height>370</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>710</width>
    <height>370</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <property name="styleSheet">
   <string notr="true"/>
  </property>
  <widget class="QProgressBar" name="progressBar">
   <property name="geometry">
    <rect>
     <x>30</x>
     <y>290</y>
     <width>641</width>
     <height>41</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">QProgressBar {
	border-radius: 20px;
	background-color: rgb(220, 231, 255);
	text-align: center;
	color:rgb(0, 0, 0);
}

QProgressBar::chunk {
	border-radius: 20px;
	background-color:rgb(58, 68, 255)
}
</string>
   </property>
   <property name="value">
    <number>24</number>
   </property>
  </widget>
  <widget class="QLabel" name="labelLogo">
   <property name="geometry">
    <rect>
     <x>150</x>
     <y>50</y>
     <width>401</width>
     <height>121</height>
    </rect>
   </property>
   <property name="text">
    <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
   </property>
  </widget>
  <widget class="QLabel" name="labelTitle">
   <property name="geometry">
    <rect>
     <x>30</x>
     <y>190</y>
     <width>641</width>
     <height>81</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: white;
font: 63 8pt &quot;Yu Gothic UI Semibold&quot;;</string>
   </property>
   <property name="text">
    <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;span style=&quot; font-size:36pt;&quot;&gt;UnitedChanger&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
   </property>
  </widget>
 </widget>
 <customwidgets>
  <customwidget>
   <class>QSplashScreen</class>
   <extends>QWidget</extends>
   <header>qsplashscreen.h</header>
   <container>1</container>
  </customwidget>
 </customwidgets>
 <resources/>
 <connections/>
</ui>
"""

LoginWindowTemplate = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>LoginWindow</class>
 <widget class="QDialog" name="LoginWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>387</width>
    <height>506</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>387</width>
    <height>506</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>387</width>
    <height>506</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color:rgb(255, 255, 255);</string>
  </property>
  <widget class="QLabel" name="LabelLogo">
   <property name="geometry">
    <rect>
     <x>60</x>
     <y>0</y>
     <width>271</width>
     <height>81</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">border: 1px solid black;
border-radius: 10px;</string>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
  <widget class="QLabel" name="LoginLabel">
   <property name="geometry">
    <rect>
     <x>70</x>
     <y>90</y>
     <width>231</width>
     <height>61</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font-size: 24px;
</string>
   </property>
   <property name="text">
    <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;span style=&quot; font-size:14pt;&quot;&gt;Login (email):&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="LoginLine">
   <property name="geometry">
    <rect>
     <x>50</x>
     <y>150</y>
     <width>271</width>
     <height>41</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font-size: 24px;
border-radius: 10px;
background-color: rgb(231, 231, 231);
border: 1px solid rgb(0, 0, 0);</string>
   </property>
   <property name="text">
    <string/>
   </property>
   <property name="echoMode">
    <enum>QLineEdit::Normal</enum>
   </property>
  </widget>
  <widget class="QLabel" name="PasswordLabel">
   <property name="geometry">
    <rect>
     <x>70</x>
     <y>200</y>
     <width>231</width>
     <height>61</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font-size: 24px;
</string>
   </property>
   <property name="text">
    <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;span style=&quot; font-size:14pt;&quot;&gt;Password:&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="PasswordLine">
   <property name="geometry">
    <rect>
     <x>50</x>
     <y>250</y>
     <width>271</width>
     <height>41</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font-size: 24px;
border-radius: 10px;
background-color: rgb(231, 231, 231);
border: 1px solid rgb(0, 0, 0);</string>
   </property>
   <property name="text">
    <string/>
   </property>
   <property name="echoMode">
    <enum>QLineEdit::Password</enum>
   </property>
  </widget>
  <widget class="QPushButton" name="EnterButton">
   <property name="geometry">
    <rect>
     <x>110</x>
     <y>320</y>
     <width>151</width>
     <height>41</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font-size: 24px;
border-radius: 10px;
background-color: rgb(240, 240, 240);
border: 1px solid rgb(0, 0, 0);</string>
   </property>
   <property name="text">
    <string>Enter</string>
   </property>
  </widget>
  <widget class="QPushButton" name="ForgotPasswordButton">
   <property name="geometry">
    <rect>
     <x>50</x>
     <y>400</y>
     <width>271</width>
     <height>31</height>
    </rect>
   </property>
   <property name="cursor">
    <cursorShape>ArrowCursor</cursorShape>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: white;
border: 1px solid rgb(255, 255, 255);
color: rgb(0, 123, 255);
text-decoration: underline;
font-size: 18px;</string>
   </property>
   <property name="text">
    <string>➝ Forgot password?</string>
   </property>
  </widget>
  <widget class="QPushButton" name="RegistrationButton">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>440</y>
     <width>341</width>
     <height>31</height>
    </rect>
   </property>
   <property name="cursor">
    <cursorShape>ArrowCursor</cursorShape>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: white;
border: 1px solid rgb(255, 255, 255);
color: rgb(0, 123, 255);
text-decoration: underline;
font-size: 18px;</string>
   </property>
   <property name="text">
    <string>➝ Don't have an account? Register.</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

RegisterWindowTemplate = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>RegisterWindow</class>
 <widget class="QDialog" name="RegisterWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>389</width>
    <height>506</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: white;</string>
  </property>
  <property name="modal">
   <bool>false</bool>
  </property>
  <widget class="QLabel" name="LoginLabel">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>110</y>
     <width>371</width>
     <height>41</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font-size: 28px;
</string>
   </property>
   <property name="text">
    <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;span style=&quot; font-size:18pt;&quot;&gt;Enter login (email):&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
   </property>
  </widget>
  <widget class="QPushButton" name="RegisterButton">
   <property name="geometry">
    <rect>
     <x>120</x>
     <y>440</y>
     <width>131</width>
     <height>41</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font-size: 24px;
border-radius: 10px;
background-color: rgb(231, 231, 231);
border: 1px solid rgb(0, 0, 0);</string>
   </property>
   <property name="text">
    <string>Register</string>
   </property>
  </widget>
  <widget class="QLabel" name="PasswordLabel1">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>220</y>
     <width>371</width>
     <height>41</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font-size: 28px;
</string>
   </property>
   <property name="text">
    <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;span style=&quot; font-size:18pt;&quot;&gt;Enter password:&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
   </property>
  </widget>
  <widget class="QLabel" name="PasswordLabel2">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>330</y>
     <width>371</width>
     <height>41</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font-size: 28px;
</string>
   </property>
   <property name="text">
    <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;span style=&quot; font-size:18pt;&quot;&gt;Enter password again:&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="LoginEntery">
   <property name="geometry">
    <rect>
     <x>60</x>
     <y>150</y>
     <width>261</width>
     <height>41</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font-size: 24px;
border-radius: 10px;
background-color: rgb(231, 231, 231);
border: 1px solid rgb(0, 0, 0);</string>
   </property>
   <property name="placeholderText">
    <string>Login (email)...</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="PasswordEntery">
   <property name="geometry">
    <rect>
     <x>60</x>
     <y>260</y>
     <width>261</width>
     <height>41</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font-size: 24px;
border-radius: 10px;
background-color: rgb(231, 231, 231);
border: 1px solid rgb(0, 0, 0);</string>
   </property>
   <property name="echoMode">
    <enum>QLineEdit::Password</enum>
   </property>
   <property name="placeholderText">
    <string>Password...</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="PasswordEnteryAgain">
   <property name="geometry">
    <rect>
     <x>60</x>
     <y>370</y>
     <width>261</width>
     <height>41</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font-size: 24px;
border-radius: 10px;
background-color: rgb(231, 231, 231);
border: 1px solid rgb(0, 0, 0);</string>
   </property>
   <property name="echoMode">
    <enum>QLineEdit::Password</enum>
   </property>
   <property name="placeholderText">
    <string>Password...</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

ForgotPasswordWindowTemplate = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>ForgotPasswordWindow</class>
 <widget class="QDialog" name="ForgotPasswordWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>459</width>
    <height>195</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: white;</string>
  </property>
  <widget class="QLabel" name="EmailEnteryLabel">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>10</y>
     <width>321</width>
     <height>61</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font-size: 36px;</string>
   </property>
   <property name="text">
    <string>Enter your email:</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="EmailLine">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>80</y>
     <width>291</width>
     <height>41</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font-size: 24px;
border-radius: 10px;
background-color: rgb(231, 231, 231);
border: 1px solid rgb(0, 0, 0);</string>
   </property>
   <property name="placeholderText">
    <string>Email...</string>
   </property>
  </widget>
  <widget class="QPushButton" name="rememberButton">
   <property name="geometry">
    <rect>
     <x>330</x>
     <y>80</y>
     <width>111</width>
     <height>41</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font-size: 20px;
border-radius: 10px;
background-color: rgb(231, 231, 231);
border: 1px solid rgb(0, 0, 0);</string>
   </property>
   <property name="text">
    <string>Send</string>
   </property>
  </widget>
  <widget class="QLabel" name="TimeLabel">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>140</y>
     <width>441</width>
     <height>41</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font-size: 30px;</string>
   </property>
   <property name="text">
    <string>Send password again in {time}.</string>
   </property>
  </widget>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>340</x>
     <y>10</y>
     <width>91</width>
     <height>61</height>
    </rect>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

UnitedChangerMainWindowTemplate = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>UnitedChangerMainWindow</class>
 <widget class="QDialog" name="UnitedChangerMainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1147</width>
    <height>636</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: white;
</string>
  </property>
  <widget class="QComboBox" name="Value1ComboBox">
   <property name="geometry">
    <rect>
     <x>30</x>
     <y>40</y>
     <width>181</width>
     <height>71</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font-size: 20px;
border: 1px solid black;
border-radius: 4px;
</string>
   </property>
  </widget>
  <widget class="QComboBox" name="Value2ComboBox">
   <property name="geometry">
    <rect>
     <x>30</x>
     <y>140</y>
     <width>181</width>
     <height>71</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font-size: 20px;
border: 1px solid black;
border-radius: 4px;
</string>
   </property>
  </widget>
  <widget class="QLabel" name="LogotypeLabel">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>250</y>
     <width>221</width>
     <height>261</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">border: 1px solid black;
border-radius: 10px;</string>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
  <widget class="QPushButton" name="settingsButton">
   <property name="geometry">
    <rect>
     <x>40</x>
     <y>550</y>
     <width>161</width>
     <height>51</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: white;
border: 1px solid black;
border-radius: 20px;
font-size: 24px;
</string>
   </property>
   <property name="text">
    <string>Settings</string>
   </property>
  </widget>
  <widget class="Line" name="line1">
   <property name="geometry">
    <rect>
     <x>243</x>
     <y>-10</y>
     <width>16</width>
     <height>641</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: black;
</string>
   </property>
   <property name="frameShadow">
    <enum>QFrame::Plain</enum>
   </property>
   <property name="lineWidth">
    <number>3</number>
   </property>
   <property name="orientation">
    <enum>Qt::Vertical</enum>
   </property>
  </widget>
  <widget class="Line" name="line2">
   <property name="geometry">
    <rect>
     <x>260</x>
     <y>300</y>
     <width>881</width>
     <height>20</height>
    </rect>
   </property>
   <property name="frameShadow">
    <enum>QFrame::Plain</enum>
   </property>
   <property name="lineWidth">
    <number>3</number>
   </property>
   <property name="orientation">
    <enum>Qt::Horizontal</enum>
   </property>
  </widget>
  <widget class="Line" name="line3">
   <property name="geometry">
    <rect>
     <x>890</x>
     <y>10</y>
     <width>20</width>
     <height>611</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: black;
</string>
   </property>
   <property name="frameShadow">
    <enum>QFrame::Plain</enum>
   </property>
   <property name="lineWidth">
    <number>3</number>
   </property>
   <property name="orientation">
    <enum>Qt::Vertical</enum>
   </property>
  </widget>
  <widget class="QGraphicsView" name="graphicsView">
   <property name="geometry">
    <rect>
     <x>260</x>
     <y>320</y>
     <width>621</width>
     <height>301</height>
    </rect>
   </property>
  </widget>
  <widget class="QScrollArea" name="scrollArea">
   <property name="geometry">
    <rect>
     <x>920</x>
     <y>400</y>
     <width>201</width>
     <height>221</height>
    </rect>
   </property>
   <property name="widgetResizable">
    <bool>true</bool>
   </property>
   <widget class="QWidget" name="scrollAreaWidgetContents">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>199</width>
      <height>219</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QLabel" name="labelValue1">
   <property name="geometry">
    <rect>
     <x>270</x>
     <y>20</y>
     <width>211</width>
     <height>61</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">border: 1px solid black;
border-radius: 20px;
font-size: 20px;</string>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
  <widget class="QLabel" name="labelValue2">
   <property name="geometry">
    <rect>
     <x>670</x>
     <y>20</y>
     <width>211</width>
     <height>61</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">border: 1px solid black;
border-radius: 20px;
font-size: 20px;</string>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
  <widget class="QLabel" name="Value1Flag">
   <property name="geometry">
    <rect>
     <x>920</x>
     <y>10</y>
     <width>211</width>
     <height>121</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">border: 1px solid whitesmoke;
border-radius: 5px;</string>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
  <widget class="QLabel" name="Value2Flag">
   <property name="geometry">
    <rect>
     <x>920</x>
     <y>160</y>
     <width>211</width>
     <height>121</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">border: 1px solid whitesmoke;
border-radius: 5px;</string>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
  <widget class="QPushButton" name="buttonEquality">
   <property name="geometry">
    <rect>
     <x>490</x>
     <y>20</y>
     <width>171</width>
     <height>61</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">border: 1px solid black;
border-radius: 20px;
font-size: 60px;
background-color: white;</string>
   </property>
   <property name="text">
    <string>⇄</string>
   </property>
  </widget>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>920</x>
     <y>330</y>
     <width>201</width>
     <height>61</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font-size: 30px;
border-radius: 10px;
border: 1px solid black;</string>
   </property>
   <property name="text">
    <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;span style=&quot; font-size:18pt;&quot;&gt;Liked Values&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
   </property>
  </widget>
  <widget class="QPushButton" name="LikedInCsvButton">
   <property name="geometry">
    <rect>
     <x>270</x>
     <y>210</y>
     <width>211</width>
     <height>71</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">border-radius: 20px; background-color: white; border: 1px solid black; font-size: 18px;</string>
   </property>
   <property name="text">
    <string>Convert Liked in CSV</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="FilenameLine">
   <property name="geometry">
    <rect>
     <x>490</x>
     <y>210</y>
     <width>201</width>
     <height>71</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">border: 1px solid black;
border-radius: 10px;
font-size: 20px;</string>
   </property>
   <property name="inputMask">
    <string/>
   </property>
   <property name="text">
    <string/>
   </property>
   <property name="placeholderText">
    <string>Filename...</string>
   </property>
  </widget>
  <widget class="QDoubleSpinBox" name="DoubleSpinConverterBox">
   <property name="geometry">
    <rect>
     <x>270</x>
     <y>110</y>
     <width>101</width>
     <height>61</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">border-radius: 5px;
border: 1px solid black;
font-size: 16px;</string>
   </property>
   <property name="maximum">
    <double>9999.989999999999782</double>
   </property>
  </widget>
  <widget class="QLabel" name="ConvertationResult">
   <property name="geometry">
    <rect>
     <x>630</x>
     <y>110</y>
     <width>131</width>
     <height>61</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">border: 1px solid black;
border-radius: 20px;
font-size: 20px;</string>
   </property>
   <property name="text">
    <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
   </property>
  </widget>
  <widget class="QComboBox" name="Converter1ComboBox">
   <property name="geometry">
    <rect>
     <x>380</x>
     <y>110</y>
     <width>141</width>
     <height>61</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font-size: 20px;
border: 1px solid black;
border-radius: 4px;
</string>
   </property>
  </widget>
  <widget class="QPushButton" name="ConvertButton">
   <property name="geometry">
    <rect>
     <x>530</x>
     <y>110</y>
     <width>91</width>
     <height>61</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">border-radius: 20px;
border: 1px solid black;
font-size: 40px;</string>
   </property>
   <property name="text">
    <string>→</string>
   </property>
  </widget>
  <widget class="QComboBox" name="Converter2ComboBox">
   <property name="geometry">
    <rect>
     <x>770</x>
     <y>110</y>
     <width>111</width>
     <height>61</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font-size: 20px;
border: 1px solid black;
border-radius: 4px;
</string>
   </property>
  </widget>
  <widget class="QPushButton" name="viewButton">
   <property name="geometry">
    <rect>
     <x>700</x>
     <y>210</y>
     <width>181</width>
     <height>71</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">border-radius: 20px; background-color: white; border: 1px solid black; font-size: 18px;</string>
   </property>
   <property name="text">
    <string>View CSV</string>
   </property>
  </widget>
  <zorder>Value1ComboBox</zorder>
  <zorder>Value2ComboBox</zorder>
  <zorder>LogotypeLabel</zorder>
  <zorder>settingsButton</zorder>
  <zorder>line1</zorder>
  <zorder>line2</zorder>
  <zorder>graphicsView</zorder>
  <zorder>scrollArea</zorder>
  <zorder>labelValue1</zorder>
  <zorder>labelValue2</zorder>
  <zorder>line3</zorder>
  <zorder>Value1Flag</zorder>
  <zorder>Value2Flag</zorder>
  <zorder>buttonEquality</zorder>
  <zorder>label</zorder>
  <zorder>LikedInCsvButton</zorder>
  <zorder>FilenameLine</zorder>
  <zorder>DoubleSpinConverterBox</zorder>
  <zorder>ConvertationResult</zorder>
  <zorder>Converter1ComboBox</zorder>
  <zorder>ConvertButton</zorder>
  <zorder>Converter2ComboBox</zorder>
  <zorder>viewButton</zorder>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

LoadingWindowTemplate = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>LoadingWindow</class>
 <widget class="QDialog" name="LoadingWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>265</width>
    <height>332</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: white;</string>
  </property>
  <widget class="QLabel" name="loadingGifLabel">
   <property name="geometry">
    <rect>
     <x>30</x>
     <y>10</y>
     <width>231</width>
     <height>201</height>
    </rect>
   </property>
   <property name="frameShape">
    <enum>QFrame::NoFrame</enum>
   </property>
   <property name="frameShadow">
    <enum>QFrame::Plain</enum>
   </property>
   <property name="text">
    <string/>
   </property>
   <property name="pixmap">
    <pixmap>../load-loading.gif</pixmap>
   </property>
  </widget>
  <widget class="QLabel" name="loadingLabel">
   <property name="geometry">
    <rect>
     <x>30</x>
     <y>220</y>
     <width>221</width>
     <height>71</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: black;
font-size: 36pt;</string>
   </property>
   <property name="text">
    <string>Loading...</string>
   </property>
  </widget>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>50</x>
     <y>290</y>
     <width>171</width>
     <height>31</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font-size: 20px;
color: black;</string>
   </property>
   <property name="text">
    <string>Wait a minute... :)</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

ViewWindowTemplate = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>ViewWindow</class>
 <widget class="QDialog" name="ViewWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1060</width>
    <height>502</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: white;</string>
  </property>
  <widget class="QTableWidget" name="ViewTable">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1061</width>
     <height>501</height>
    </rect>
   </property>
   <property name="sizeAdjustPolicy">
    <enum>QAbstractScrollArea::AdjustToContents</enum>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""