---
app_name: Computerized Patient Record System (CPRS)
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: null
doc_type: user-manual
fetch_format: ''
forum_patch_stub: false
ingest_date: '2026-03-11'
is_base: false
is_change_pages: false
library_max_patch: null
package_id: CPRS
patch: null
patch_gap: null
section: ''
source_file: or_3_p529_qr.docx
status: draft
title: or 3 p529 qr.docx
---

<!-- image -->

This patch provides functionality to maintain continuity of care during a site's Cerner cutover by creating a report of recent clinical activity for every patient seen in the last three years that providers can cross-reference during the initial cutover period. This is done by automatically creating documents for a single, user-selected patient, or to initiate a task to create a document for every patient that has had an inpatient, outpatient, or clinic visit in the past three years.

**Note** :	The *VistA Cutover Utilities Menu* is locked by the ORVCO Security Key.

### VistA Cutover Utilities Menu

1. Run System Benchmark
2. Test Data Retrieval
3. Create VistA Cutover Document(s)
4. Monitor/Stop Cutover Jobs (optional)

**Select VistA Cutover &lt;TEST ACCOUNT&gt; Option** :

**Note** :	Before you begin testing or creating cutover documents, it is highly recommended to run the CPRS Coversheet Time Test released with CPRS 31b.

**Optional Step** - Run the CPRS Coversheet Time Test [PXRM CPRS TESTER]

The CPRS Coversheet Time Test is optional but will provide essential timing information when testing or creating the clinical reminders cutover document. The clinical reminders cutover document uses the reminders included on the CPRS Coversheet and places that information into the document text.

The main pieces of information to evaluate from the results are:

- Elapsed wall clock time
- Total CPU coversheet evaluation time
- Longest CPU evaluation time
- Longest wall clock evaluation time.”

If the CPRS Coversheet Time Test reports an “Elapsed wall clock time” of less than 1 second, move to Step 1 below.

If the “Elapsed wall clock time” is 1 second or higher, it is highly suggested to remove reminders from the CPRS coversheet settings that require the longest time to evaluate and/or the most CPU time.  After making changes, perform the time test again to verify the improvement. The goal is to reduce the “Elapsed wall clock time” as low as possible while keeping as many of the desired reminders for the cutover document.

*(Continued from bottom of Column 1)*

Take note of your final “Elapsed wall clock time.” This time will be used to help estimate the total amount of time for the Clinical Reminders Cutover document.

**Example output below from the last sections of the CPRS Coversheet Time Test** :

Total number of reminders evaluated: 59

**Elapsed wall clock time: 173 seconds**

**Total CPU coversheet evaluation time: 9995 milliseconds**

**Longest CPU evaluation time**

**Reminder: VA-CRC AVERAGE RISK (IEN=306)**

**Reminder CPU evaluation time: 2064 milliseconds**

**Longest wall clock evaluation time**

**Reminder: VA-CRC AVERAGE RISK (IEN=306)**

**Reminder wall clock evaluation time: 37 seconds**

**Note** :	There are some national and local reminders that will take an extremely long time to evaluate. Any reminder with a “Reminder wall clock time” greater than 1 second should be removed from the default reminders for the CPRS coversheet.

**Step 1 - Run System Benchmark**

1. Select Option 1 from the VistA Cutover Utilities menu. The benchmark will find patients to use for the benchmark testing. The test will take approximately five minutes to complete. Results of each test will display when finished and the benchmark will automatically set the optimum number of threads for the Test and Create options.

**Benchmark Tool                :37:39**

**# of   Patients    Total     Avg      Max      Est.     Time to**

**Test   Threads   Processed   Time    Thread   Pt/Sec   Completion**

**1        1         2286       31     30.00     76.20  15 min 34 sec**

**2        5         6931       33     30.00    231.03   5 min 08 sec**

**3        10        9848       33     28.00    351.71   3 min 22 sec**

**4        15        10000      30     24.20    413.22   2 min 52 sec**

**5        20        10000      26     22.15    451.47   2 min 38 sec**

**6        25        10000      23     20.08    498.01   2 min 23 sec**

**7        30        10000      22     18.90    529.10   2 min 15 sec**

**8        35        10000      23     19.43    514.67   2 min 18 sec**

**9        40        10000      24     20.40    490.20   2 min 25 sec**

**&lt; Benchmark Testing Complete &gt;**

**Press &lt;ENTER&gt; to continue**

**Note:** The estimated time to completion may vary significantly based on the difference in clinical data from the initial patients used for the benchmark versus the remaining patients and the amount of data needed to process. The number of threads to use is chosen based on your system’s current performance.

<!-- image -->

1. Select Option 2 from the VistA Cutover Utilities menu.
When asked, “Do you wish to select a single patient?” **enter NO and press &lt;Enter&gt;**
2. When asked, “Do you wish to test the Clinical Reminders cutover documents?” **accept the default entry of NO and press &lt;Enter&gt;**
3. When asked, “Continue for all patients?” **enter YES and press &lt;Enter&gt;.** A screen showing the progress of patient evaluation will display. Once all patients have been evaluated, the test process will begin. It is possible for the number of patients evaluated to be higher or lower than the number of total patients. The total patients are reported by FileMan and the evaluated patients are an actual count of the patient file.

**Example output from the patient evaluation phase:**

Evaluating patients...110927 of 110927

65804 patients will be tested for the EHRM Cutover.

Press &lt;ENTER&gt; to continue

**Note:** The number of patients that meet the criteria that will be tested should match exactly in the summary email received by the user at the completion of the test **.**

**Tip** :	Multiply the “Elapsed wall clock time” by the number of patients that will be tested to find the minimum amount of time in seconds to complete the clinical reminders test or document creation.

**Daemon* Monitoring Tool                      11:10:09**

**Active**

**Job #   User       Progress  Mode    Type    Threads      Start Date/Time**

**7523 PATIENT,ONE   33%       Test  Summary   24 of 25     Nov 05, 2020@11:09**

**Enter monitor action: UPDATE//**

- **In multitasking computer operating systems, a Daemon is a computer program that runs as a background process rather than being under the direct control of an interactive user**

<!-- image -->

**Step 3 – Run the Create VistA Cutover Document(s)**

1. Select option 3 from the VistA Cutover Utilities menu.
2. Please see your site’s schedule for cutover tasks before initiating either the summary or reminders document in Production.
3. Once the job has finished, the user will receive a summary email message.

**Note:** Wait for the summary document creation to complete before beginning the reminders document creation.

**Run the Monitor/Stop Cutover Jobs (Optional)**

**Option 4** from the Vista Cutover Utilities menu allows the user to take actions while the cutover process is running, if necessary. There are 3 available actions: **UPDATE (default)** , **STOP** , or **QUIT** .

- Pressing **&lt;Enter&gt;** will **UPDATE** the progress of the job(s), allowing the user to track progress real time. It is normal for the active threads to decrease as they finish but before the overall progress is 100%.
- Entering **STOP** will prompt the user for the job # they wish to ask TaskMan to stop running. It can take several minutes for all of the running threads to cease activity. Once they have all stopped, the summary email will still be sent to the initiating user with partial results **[Stopped by Task Manager]** and will be included in the body of the message.
- Once both the summary and clinical reminders processes have finished in TEST mode, the total amount of time for each will be approximately 5-10% longer during the document creation process.

**Example output from the monitoring tool:**