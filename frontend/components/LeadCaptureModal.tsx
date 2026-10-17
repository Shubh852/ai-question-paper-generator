'use client';

import React, { useState } from 'react';
import { X, Download, ShieldCheck, Sparkles, School, User, MapPin, Phone } from 'lucide-react';

interface LeadCaptureModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSuccessDownload: () => void;
  examId?: string;
  documentType: 'student' | 'solution';
}

export default function LeadCaptureModal({
  isOpen,
  onClose,
  onSuccessDownload,
  examId,
  documentType
}: LeadCaptureModalProps) {
  const [teacherName, setTeacherName] = useState('');
  const [schoolName, setSchoolName] = useState('');
  const [city, setCity] = useState('');
  const [whatsapp, setWhatsapp] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  if (!isOpen) return null;

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!teacherName || !schoolName || !city || !whatsapp) {
      setError('Please fill in all details to unlock your print-ready PDF.');
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const res = await fetch('/api/v1/capture-lead', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          teacher_name: teacherName,
          school_name: schoolName,
          city: city,
          whatsapp_number: whatsapp,
          generated_exam_id: examId || null,
        }),
      });

      if (!res.ok) {
        throw new Error('Could not save teacher details. Please try again.');
      }

      // Trigger the download callback
      onSuccessDownload();
      onClose();
    } catch (err: any) {
      setError(err.message || 'Something went wrong');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/60 p-4 backdrop-blur-sm animate-in fade-in duration-200">
      <div className="relative w-full max-w-lg rounded-2xl bg-white p-6 shadow-2xl ring-1 ring-slate-900/10 sm:p-8">
        <button
          onClick={onClose}
          className="absolute right-4 top-4 rounded-full p-1.5 text-slate-400 hover:bg-slate-100 hover:text-slate-600 transition-colors"
        >
          <X className="h-5 w-5" />
        </button>

        <div className="flex items-center space-x-3 mb-2">
          <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-blue-100 text-blue-700">
            <Sparkles className="h-5 w-5" />
          </div>
          <div>
            <h3 className="text-xl font-bold text-slate-900">
              Download {documentType === 'solution' ? 'Step-Wise Marking Scheme' : 'Question Paper'}
            </h3>
            <p className="text-xs text-slate-500">
              High-resolution, unwatermarked PDF compiled via Typst
            </p>
          </div>
        </div>

        <div className="my-4 rounded-xl bg-blue-50/70 p-3 text-xs text-blue-800 border border-blue-200/60 flex items-center space-x-2">
          <ShieldCheck className="h-4 w-4 flex-shrink-0 text-blue-600" />
          <span>
            Enter your teacher credentials once to unlock free downloads & answer keys across all classes.
          </span>
        </div>

        {error && (
          <div className="mb-4 rounded-lg bg-red-50 p-2.5 text-xs text-red-600 border border-red-200">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1">
              Teacher / Educator Name *
            </label>
            <div className="relative">
              <User className="absolute left-3 top-2.5 h-4 w-4 text-slate-400" />
              <input
                type="text"
                required
                placeholder="e.g. Dr. Rajesh Sharma"
                value={teacherName}
                onChange={(e) => setTeacherName(e.target.value)}
                className="w-full rounded-lg border border-slate-300 py-2 pl-9 pr-3 text-sm focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500"
              />
            </div>
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1">
              School / Coaching Institute Name *
            </label>
            <div className="relative">
              <School className="absolute left-3 top-2.5 h-4 w-4 text-slate-400" />
              <input
                type="text"
                required
                placeholder="e.g. Delhi Public School / Allen"
                value={schoolName}
                onChange={(e) => setSchoolName(e.target.value)}
                className="w-full rounded-lg border border-slate-300 py-2 pl-9 pr-3 text-sm focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500"
              />
            </div>
          </div>

          <div className="grid grid-cols-2 gap-3">
            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1">
                City / State *
              </label>
              <div className="relative">
                <MapPin className="absolute left-3 top-2.5 h-4 w-4 text-slate-400" />
                <input
                  type="text"
                  required
                  placeholder="e.g. Mumbai, MH"
                  value={city}
                  onChange={(e) => setCity(e.target.value)}
                  className="w-full rounded-lg border border-slate-300 py-2 pl-9 pr-3 text-sm focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500"
                />
              </div>
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1">
                WhatsApp Number *
              </label>
              <div className="relative">
                <Phone className="absolute left-3 top-2.5 h-4 w-4 text-slate-400" />
                <input
                  type="tel"
                  required
                  placeholder="+91 98765 43210"
                  value={whatsapp}
                  onChange={(e) => setWhatsapp(e.target.value)}
                  className="w-full rounded-lg border border-slate-300 py-2 pl-9 pr-3 text-sm focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500"
                />
              </div>
            </div>
          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full flex items-center justify-center space-x-2 rounded-xl bg-blue-600 py-3 text-sm font-semibold text-white shadow-md hover:bg-blue-700 active:scale-[0.99] transition-all disabled:opacity-50"
          >
            {loading ? (
              <span className="flex items-center space-x-2">
                <span className="h-4 w-4 animate-spin rounded-full border-2 border-white border-t-transparent"></span>
                <span>Generating Print PDF...</span>
              </span>
            ) : (
              <>
                <Download className="h-4 w-4" />
                <span>Unlock & Download PDF Now</span>
              </>
            )}
          </button>
        </form>

        <p className="mt-4 text-center text-[11px] text-slate-400">
          We respect educator privacy. Instant PDF delivery without spam.
        </p>
      </div>
    </div>
  );
}
