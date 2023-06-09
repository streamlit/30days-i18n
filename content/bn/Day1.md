# একটি লোকাল ডেভেলপমেন্ট পরিবেশ স্থাপন

আসলে স্ট্রিমলিট অ্যাপ তৈরি করা শুরু করার আগে, আমাদের প্রথমে ডেভেলপমেন্টের জন্য পরিবেশ সেটআপ করতে হবে।

আসুন একটি কনডা পরিবেশ ইনস্টল এবং সেট আপ করে শুরু করি।

## **কনডা ইনস্টল**
- `conda` ইনস্টল এখানে https://docs.conda.io/en/latest/miniconda.html. আপনি অপারেটিং সিস্টেম বেছে নিন (উইন্ডোস, ম্যাক বা লিনাক্স). 
- ইনস্টল করার জন্য ইনস্টলারটি ডাউনলোড করুন এবং `conda` চালান।

## **একটি নতুন কনডা পরিবেশ তৈরি করুন**

এখন যেহেতু আপনি কনডা ইনস্টল করেছেন, আসুন পাইথন লাইব্রেরির সমস্ত নির্ভরতা পরিচালনা করার জন্য একটি কনডা পরিবেশ তৈরি করি।

পাইথন ৩.৯ এর সাথে একটি নতুন পরিবেশ তৈরি করতে, নিম্নলিখিতটি প্রবেশ করান:
```bash
conda create -n stenv python=3.9
```

যেখানে `create -n stenv` একটি কনডা পরিবেশ তৈরি করবে যার নাম `stenv` এবং `python=3.9` সেটআপ পরিবেশ তৈরী করবে যার সংস্করণ ৩.৯।

## **কনডা পরিবেশ সক্রিয় করুন**

তৈরী করা কনডা পরিবেশ যার নাম `stenv`, কোমান্ড লাইনে টাইপ করুন:

```bash
conda activate stenv
```

## **স্ট্রিমলিট লাইব্রেরি ইনস্টল করুন**

এখনি `streamlit` লাইব্রেরি ইনস্টল করার সময়:
```bash
pip install streamlit
```

## **স্ট্রিমলিট ডেমো অ্যাপ চালু করা**
অ্যাপ চালু করতে:
```bash
streamlit hello
```
