'use client';

import React, { useState } from 'react';
import {
  Sparkles,
  FileCheck2,
  UploadCloud,
  CheckCircle2,
  Clock,
  ArrowRight,
  ShieldCheck,
  Zap,
  X,
  MessageCircle,
  HelpCircle,
  Award,
  BookOpen
} from 'lucide-react';

export interface AiCopyCheckerModalProps {
  isOpen: boolean;
  onClose: () => void;
  currentUser?: {
    id?: string;
    name?: string;
    school?: string;
    city?: string;
    email?: string;
    whatsapp?: string;
  } | null;
  examContext?: {
    title?: string;
    grade?: number;
    subject?: string;
    examId?: string;
  } | null;
}

export default function AiCopyCheckerModal({
  isOpen,
  onClose,
  currentUser,
  examContext
}: AiCopyCheckerModalProps) {
  const [name, setName] = useState(currentUser?.name || '');
  const [school, setSchool] = useState(currentUser?.school || '');
  const [whatsapp, setWhatsapp] = useState(currentUser?.whatsapp || '');
  const [city, setCity] = useState(currentUser?.city || '');
  const [email, setEmail] = useState(currentUser?.email || '');
  const [sampleUploaded, setSampleUploaded] = useState(false);
  const [fileName, setFileName] = useState<string | null>(null);
  const [submitting, setSubmitting] = useState(false);
  const [submitted, setSubmitted] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Sync state if currentUser changes
  React.useEffect(() => {
    if (currentUser) {
      if (currentUser.name && !name) setName(currentUser.name);
      if (currentUser.school && !school) setSchool(currentUser.school);
      if (currentUser.whatsapp && !whatsapp) setWhatsapp(currentUser.whatsapp);
      if (currentUser.city && !city) setCity(currentUser.city);
      if (currentUser.email && !email) setEmail(currentUser.email);
    }
  }, [currentUser]);

  if (!isOpen) return null;

  const supportWhatsapp = process.env.NEXT_PUBLIC_SUPPORT_WHATSAPP || '919876543210';

  const handleFileUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      setFileName(file.name);
      setSampleUploaded(true);
    }
  };

  const handleSubmitLead = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!name.trim() || !school.trim() || !whatsapp.trim()) {
      setError('Please provide your Name, School Name, and WhatsApp Number.');
      return;
    }
    setError(null);
    setSubmitting(true);

    try {
      const res = await fetch('/api/v1/copy-checker-lead', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          teacher_name: name.trim(),
          school_name: school.trim(),
          city: city.trim() || 'Not specified',
          whatsapp_number: whatsapp.trim(),
          email: email.trim() || undefined,
          grade_level: examContext?.grade || 10,
          subject: examContext?.subject || 'All Subjects',
          exam_id: examContext?.examId || undefined,
          notes: fileName ? `Sample PDF attached: ${fileName}` : 'Interested in ₹500 AI Copy Checking batch.'
        })
      });

      if (!res.ok) {
        throw new Error('Failed to register request. Please try again.');
      }

      setSubmitted(true);
    } catch (err: any) {
      setError(err.message || 'Submission error');
    } finally {
      setSubmitting(false);
    }
  };

  const getWhatsAppChatUrl = () => {
    const text = encodeURIComponent(
      `Hello! I want to try AI Student Copy Checking for ₹500 for my school (${school || 'My School'}). ` +
      `Teacher: ${name || 'Educator'}, Subject: ${examContext?.subject || 'Mathematics/Science'}, ` +
      `Grade: Class ${examContext?.grade || '10'}. Please share the onboarding steps!`
    );
    return `https://wa.me/${supportWhatsapp.replace(/[^0-9]/g, '')}?text=${text}`;
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm animate-fade-in overflow-y-auto">
      <div className="relative w-full max-w-2xl bg-white rounded-3xl shadow-2xl border border-slate-200 overflow-hidden my-8">
        {/* Top Gradient Banner */}
        <div className="bg-gradient-to-r from-blue-700 via-indigo-700 to-purple-800 p-6 text-white relative">
          <button
            onClick={onClose}
            className="absolute top-5 right-5 p-1.5 rounded-full bg-white/10 hover:bg-white/20 text-white transition-colors"
          >
            <X className="h-5 w-5" />
          </button>

          <div className="inline-flex items-center space-x-1.5 bg-amber-400 text-amber-950 px-3 py-1 rounded-full text-xs font-black shadow-md uppercase tracking-wider mb-2">
            <Zap className="h-3.5 w-3.5 fill-current" />
            <span>Introductory Offer: Just ₹500 / Batch</span>
          </div>

          <h2 className="text-2xl sm:text-3xl font-black tracking-tight flex items-center gap-2">
            AI Student Copy Evaluator
          </h2>
          <p className="text-blue-100 text-xs sm:text-sm mt-1 max-w-xl">
            Never spend weekends manual-grading 40+ copies again. Upload handwritten student copies (PDF) 
            and our AI grades each step strictly according to official CBSE marking rubrics!
          </p>
        </div>

        {/* Modal Body */}
        <div className="p-6 sm:p-8 space-y-6 max-h-[75vh] overflow-y-auto">
          {submitted ? (
            <div className="text-center py-6 space-y-4">
              <div className="h-16 w-16 bg-emerald-100 text-emerald-600 rounded-full flex items-center justify-center mx-auto shadow-inner">
                <CheckCircle2 className="h-9 w-9" />
              </div>
              <h3 className="text-xl font-black text-slate-900">
                You’re on the ₹500 VIP Early Access List!
              </h3>
              <p className="text-xs sm:text-sm text-slate-600 max-w-md mx-auto leading-relaxed">
                Thank you, <strong>{name}</strong>! We have recorded your interest for <strong>{school}</strong>. 
                Our Academic AI Specialist will connect with you via WhatsApp at <strong>{whatsapp}</strong> to activate 
                your ₹500 evaluation batch.
              </p>

              <div className="pt-4 flex flex-col sm:flex-row items-center justify-center gap-3">
                <a
                  href={getWhatsAppChatUrl()}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="w-full sm:w-auto inline-flex items-center justify-center space-x-2 bg-emerald-600 hover:bg-emerald-700 text-white px-6 py-3 rounded-xl font-bold text-xs shadow-md transition-all"
                >
                  <MessageCircle className="h-4 w-4" />
                  <span>Chat with Us on WhatsApp Now</span>
                </a>
                <button
                  type="button"
                  onClick={onClose}
                  className="w-full sm:w-auto border border-slate-300 text-slate-700 hover:bg-slate-100 px-5 py-3 rounded-xl font-bold text-xs transition-all"
                >
                  Back to Question Papers
                </button>
              </div>
            </div>
          ) : (
            <>
              {/* 3 Step Explanation Flow */}
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
                <div className="bg-slate-50 border border-slate-200 rounded-2xl p-3.5 text-center">
                  <div className="h-8 w-8 bg-blue-100 text-blue-600 rounded-xl flex items-center justify-center mx-auto mb-2">
                    <UploadCloud className="h-4 w-4" />
                  </div>
                  <h4 className="text-xs font-bold text-slate-900">1. Upload Copies</h4>
                  <p className="text-[11px] text-slate-500 mt-1 leading-snug">
                    Upload scanned student answer sheets in bulk as a single PDF.
                  </p>
                </div>

                <div className="bg-slate-50 border border-slate-200 rounded-2xl p-3.5 text-center">
                  <div className="h-8 w-8 bg-purple-100 text-purple-600 rounded-xl flex items-center justify-center mx-auto mb-2">
                    <FileCheck2 className="h-4 w-4" />
                  </div>
                  <h4 className="text-xs font-bold text-slate-900">2. CBSE Step-Marking</h4>
                  <p className="text-[11px] text-slate-500 mt-1 leading-snug">
                    Evaluates formulas, calculations, and theorems with fractional marks.
                  </p>
                </div>

                <div className="bg-slate-50 border border-slate-200 rounded-2xl p-3.5 text-center">
                  <div className="h-8 w-8 bg-emerald-100 text-emerald-600 rounded-xl flex items-center justify-center mx-auto mb-2">
                    <Award className="h-4 w-4" />
                  </div>
                  <h4 className="text-xs font-bold text-slate-900">3. Red-Pen Results</h4>
                  <p className="text-[11px] text-slate-500 mt-1 leading-snug">
                    Download evaluated copies with annotations & student scorecards.
                  </p>
                </div>
              </div>

              {/* Pricing Callout */}
              <div className="bg-gradient-to-r from-amber-50 to-orange-50 border border-amber-200 rounded-2xl p-4 flex items-center justify-between">
                <div>
                  <div className="text-[10px] font-bold uppercase tracking-wider text-amber-800">
                    School Pilot Pricing
                  </div>
                  <div className="flex items-baseline space-x-2">
                    <span className="text-2xl font-black text-slate-900">₹500</span>
                    <span className="text-xs text-slate-400 line-through">₹2,000</span>
                    <span className="text-xs font-bold text-emerald-700 bg-emerald-100 px-2 py-0.5 rounded-full">
                      75% OFF • Up to 40 Copies
                    </span>
                  </div>
                  <div className="text-[11px] text-slate-600 mt-0.5">
                    Less than ₹12.50 per student for complete multi-page grading!
                  </div>
                </div>

                <div className="hidden sm:block text-right">
                  <span className="text-[10px] text-amber-700 font-bold bg-amber-100 border border-amber-300 px-2.5 py-1 rounded-full">
                    ⚡ Verified CBSE Rubrics
                  </span>
                </div>
              </div>

              {/* Sample Upload Dropzone Mockup */}
              <div className="border-2 border-dashed border-indigo-200 bg-indigo-50/40 rounded-2xl p-4 text-center">
                <input
                  type="file"
                  id="sampleCopyUpload"
                  accept=".pdf,image/*"
                  onChange={handleFileUpload}
                  className="hidden"
                />
                <label
                  htmlFor="sampleCopyUpload"
                  className="cursor-pointer flex flex-col items-center justify-center space-y-1.5"
                >
                  <div className="h-10 w-10 bg-indigo-100 text-indigo-600 rounded-full flex items-center justify-center">
                    <UploadCloud className="h-5 w-5" />
                  </div>
                  <div className="text-xs font-bold text-indigo-900">
                    {fileName ? (
                      <span className="text-emerald-700 flex items-center gap-1">
                        <CheckCircle2 className="h-4 w-4" /> {fileName} selected
                      </span>
                    ) : (
                      'Upload a Sample Student Copy (.pdf or images)'
                    )}
                  </div>
                  <span className="text-[10px] text-slate-500">
                    Optional: Upload 1 student copy to get a free evaluated demo
                  </span>
                </label>
              </div>

              {/* Lead Request Form */}
              <form onSubmit={handleSubmitLead} className="space-y-4">
                {error && (
                  <div className="rounded-xl bg-red-50 border border-red-200 p-3 text-xs text-red-700">
                    {error}
                  </div>
                )}

                <div className="grid grid-cols-1 sm:grid-cols-2 gap-3.5">
                  <div>
                    <label className="block text-xs font-bold text-slate-700 mb-1">
                      Educator Name <span className="text-red-500">*</span>
                    </label>
                    <input
                      type="text"
                      required
                      value={name}
                      onChange={(e) => setName(e.target.value)}
                      placeholder="e.g. Dr. Ananya Sharma"
                      className="w-full rounded-xl border border-slate-200 px-3 py-2 text-xs font-medium text-slate-900 focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500"
                    />
                  </div>

                  <div>
                    <label className="block text-xs font-bold text-slate-700 mb-1">
                      School Name <span className="text-red-500">*</span>
                    </label>
                    <input
                      type="text"
                      required
                      value={school}
                      onChange={(e) => setSchool(e.target.value)}
                      placeholder="e.g. Delhi Public School"
                      className="w-full rounded-xl border border-slate-200 px-3 py-2 text-xs font-medium text-slate-900 focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500"
                    />
                  </div>
                </div>

                <div className="grid grid-cols-1 sm:grid-cols-2 gap-3.5">
                  <div>
                    <label className="block text-xs font-bold text-slate-700 mb-1">
                      WhatsApp Number <span className="text-red-500">*</span>
                    </label>
                    <input
                      type="tel"
                      required
                      value={whatsapp}
                      onChange={(e) => setWhatsapp(e.target.value)}
                      placeholder="+91 98765 43210"
                      className="w-full rounded-xl border border-slate-200 px-3 py-2 text-xs font-medium text-slate-900 focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500"
                    />
                  </div>

                  <div>
                    <label className="block text-xs font-bold text-slate-700 mb-1">
                      City / Location
                    </label>
                    <input
                      type="text"
                      value={city}
                      onChange={(e) => setCity(e.target.value)}
                      placeholder="e.g. New Delhi"
                      className="w-full rounded-xl border border-slate-200 px-3 py-2 text-xs font-medium text-slate-900 focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500"
                    />
                  </div>
                </div>

                {examContext && (
                  <div className="bg-slate-100 rounded-xl p-2.5 flex items-center justify-between text-xs text-slate-600">
                    <span className="font-semibold">Associated Paper:</span>
                    <span className="font-bold text-blue-700">
                      Class {examContext.grade} {examContext.subject} ({examContext.title || 'Current Exam'})
                    </span>
                  </div>
                )}

                <div className="pt-2 flex flex-col sm:flex-row items-center gap-3">
                  <button
                    type="submit"
                    disabled={submitting}
                    className="w-full sm:flex-1 py-3 px-4 rounded-xl bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 text-white font-bold text-xs shadow-md transition-all disabled:opacity-50 flex items-center justify-center space-x-2"
                  >
                    <Zap className="h-4 w-4" />
                    <span>{submitting ? 'Registering...' : 'Claim Early Access @ ₹500'}</span>
                  </button>

                  <a
                    href={getWhatsAppChatUrl()}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="w-full sm:w-auto py-3 px-4 rounded-xl border border-emerald-500 bg-emerald-50 text-emerald-800 hover:bg-emerald-100 font-bold text-xs transition-all flex items-center justify-center space-x-1.5"
                  >
                    <MessageCircle className="h-4 w-4 text-emerald-600" />
                    <span>WhatsApp Inquiry</span>
                  </a>
                </div>

                <p className="text-[10px] text-center text-slate-400">
                  🔒 We respect educator privacy. No spam. Your phone number is only used to send demo results.
                </p>
              </form>
            </>
          )}
        </div>
      </div>
    </div>
  );
}
