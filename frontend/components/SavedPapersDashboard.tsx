'use client';

import React, { useState, useEffect } from 'react';

interface SavedExam {
  id: string;
  title: string;
  grade_level: number;
  subject: string;
  total_marks: number;
  duration_minutes: number;
  exam_type: string;
  selected_chapters: string[];
  blueprint_breakdown?: Record<string, number>;
  question_ids?: string[];
  student_pdf_url?: string;
  solution_pdf_url?: string;
  created_at?: string;
}

interface SavedPapersDashboardProps {
  onLoadExamToPreview?: (examId: string) => void;
  onSwitchToGenerator?: () => void;
}

export default function SavedPapersDashboard({
  onLoadExamToPreview,
  onSwitchToGenerator,
}: SavedPapersDashboardProps) {
  const [exams, setExams] = useState<SavedExam[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [searchTerm, setSearchTerm] = useState('');
  const [filterSubject, setFilterSubject] = useState('ALL');
  const [downloadingId, setDownloadingId] = useState<string | null>(null);

  const fetchSavedExams = async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await fetch('http://127.0.0.1:8000/api/v1/saved-exams');
      if (!res.ok) throw new Error('Failed to fetch saved question papers');
      const data = await res.json();
      setExams(data.exams || []);
    } catch (err: any) {
      setError(err.message || 'Error connecting to database');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchSavedExams();
  }, []);

  const handleDelete = async (id: string, e: React.MouseEvent) => {
    e.stopPropagation();
    if (!confirm('Are you sure you want to delete this saved question paper?')) return;
    try {
      const res = await fetch(`http://127.0.0.1:8000/api/v1/saved-exams/${id}`, {
        method: 'DELETE',
      });
      if (!res.ok) throw new Error('Failed to delete paper');
      setExams(exams.filter((ex) => ex.id !== id));
    } catch (err: any) {
      alert(`Could not delete: ${err.message}`);
    }
  };

  const handleDownload = async (id: string, type: 'student' | 'solution', title: string) => {
    setDownloadingId(`${id}-${type}`);
    try {
      const url = `http://127.0.0.1:8000/api/v1/download-pdf/${id}?doc=${type}`;
      const res = await fetch(url);
      if (!res.ok) throw new Error('Failed to generate PDF download');
      const blob = await res.blob();
      const blobUrl = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = blobUrl;
      a.download = `${title.replace(/\s+/g, '_')}_${type === 'solution' ? 'Solution_Scheme' : 'Student_Paper'}.pdf`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      window.URL.revokeObjectURL(blobUrl);
    } catch (err: any) {
      alert(`Download failed: ${err.message}`);
    } finally {
      setDownloadingId(null);
    }
  };

  const subjects = ['ALL', ...Array.from(new Set(exams.map((e) => e.subject)))];

  const filteredExams = exams.filter((e) => {
    const matchesSearch =
      e.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
      e.subject.toLowerCase().includes(searchTerm.toLowerCase()) ||
      (e.selected_chapters || []).some((c) => c.toLowerCase().includes(searchTerm.toLowerCase()));
    const matchesSubject = filterSubject === 'ALL' || e.subject === filterSubject;
    return matchesSearch && matchesSubject;
  });

  return (
    <div className="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
      {/* Top Banner & Stats */}
      <div className="mb-6 flex flex-col justify-between gap-4 sm:flex-row sm:items-center">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-slate-900 sm:text-3xl">
            My Saved Question Papers
          </h1>
          <p className="mt-1 text-sm text-slate-500">
            Revisit, re-download, or customize past CBSE examinations and periodic tests.
          </p>
        </div>
        <div className="flex items-center gap-3">
          <button
            onClick={fetchSavedExams}
            className="inline-flex items-center gap-1.5 rounded-lg border border-slate-300 bg-white px-3.5 py-2 text-sm font-semibold text-slate-700 shadow-sm transition hover:bg-slate-50"
          >
            <svg className="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
            Refresh
          </button>
          {onSwitchToGenerator && (
            <button
              onClick={onSwitchToGenerator}
              className="inline-flex items-center gap-2 rounded-lg bg-indigo-600 px-4 py-2 text-sm font-semibold text-white shadow-sm transition hover:bg-indigo-700"
            >
              <span>+ Create New Paper</span>
            </button>
          )}
        </div>
      </div>

      {/* Metrics Row */}
      <div className="mb-6 grid grid-cols-2 gap-4 sm:grid-cols-4">
        <div className="rounded-xl border border-slate-200 bg-white p-4 shadow-sm">
          <span className="text-xs font-medium uppercase tracking-wider text-slate-500">Total Papers</span>
          <p className="mt-1 text-2xl font-bold text-slate-900">{exams.length}</p>
        </div>
        <div className="rounded-xl border border-slate-200 bg-white p-4 shadow-sm">
          <span className="text-xs font-medium uppercase tracking-wider text-slate-500">Subjects Covered</span>
          <p className="mt-1 text-2xl font-bold text-indigo-600">{subjects.length > 1 ? subjects.length - 1 : 0}</p>
        </div>
        <div className="rounded-xl border border-slate-200 bg-white p-4 shadow-sm">
          <span className="text-xs font-medium uppercase tracking-wider text-slate-500">Grades</span>
          <p className="mt-1 text-2xl font-bold text-emerald-600">
            {Array.from(new Set(exams.map((e) => e.grade_level))).sort().join(', ') || '10, 11, 12'}
          </p>
        </div>
        <div className="rounded-xl border border-slate-200 bg-white p-4 shadow-sm">
          <span className="text-xs font-medium uppercase tracking-wider text-slate-500">PDF Engine</span>
          <p className="mt-1 text-2xl font-bold text-amber-600">Typst Print</p>
        </div>
      </div>

      {/* Filter / Search Bar */}
      <div className="mb-6 flex flex-col gap-3 rounded-xl border border-slate-200 bg-white p-4 shadow-sm sm:flex-row sm:items-center">
        <div className="relative flex-1">
          <input
            type="text"
            placeholder="Search by title, subject, or chapter..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full rounded-lg border border-slate-300 py-2 pl-9 pr-4 text-sm text-slate-900 placeholder-slate-400 focus:border-indigo-500 focus:outline-none focus:ring-1 focus:ring-indigo-500"
          />
          <svg
            className="absolute left-3 top-2.5 h-4 w-4 text-slate-400"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
        </div>
        <div className="flex items-center gap-2 overflow-x-auto pb-1 sm:pb-0">
          <span className="text-xs font-medium text-slate-500">Subject:</span>
          {subjects.map((sub) => (
            <button
              key={sub}
              onClick={() => setFilterSubject(sub)}
              className={`whitespace-nowrap rounded-lg px-3 py-1.5 text-xs font-semibold transition ${
                filterSubject === sub
                  ? 'bg-indigo-600 text-white'
                  : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
              }`}
            >
              {sub}
            </button>
          ))}
        </div>
      </div>

      {/* Loading & Error States */}
      {loading && (
        <div className="py-20 text-center">
          <div className="inline-block h-8 w-8 animate-spin rounded-full border-4 border-indigo-600 border-t-transparent"></div>
          <p className="mt-3 text-sm text-slate-500">Loading saved question papers...</p>
        </div>
      )}

      {error && (
        <div className="rounded-xl border border-red-200 bg-red-50 p-4 text-center text-sm text-red-700">
          {error}
        </div>
      )}

      {/* Empty State */}
      {!loading && !error && filteredExams.length === 0 && (
        <div className="rounded-2xl border-2 border-dashed border-slate-300 bg-white py-16 text-center">
          <div className="mx-auto mb-3 flex h-14 w-14 items-center justify-center rounded-full bg-indigo-50 text-indigo-600">
            <svg className="h-7 w-7" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
          </div>
          <h3 className="text-base font-bold text-slate-900">No saved papers found</h3>
          <p className="mt-1 text-sm text-slate-500">
            {searchTerm || filterSubject !== 'ALL'
              ? 'Try adjusting your search query or subject filters.'
              : 'You have not generated any exam papers yet.'}
          </p>
          {onSwitchToGenerator && (
            <button
              onClick={onSwitchToGenerator}
              className="mt-4 inline-flex items-center gap-2 rounded-lg bg-indigo-600 px-4 py-2 text-sm font-semibold text-white shadow hover:bg-indigo-700"
            >
              Generate Your First Exam Paper
            </button>
          )}
        </div>
      )}

      {/* Exam Cards Grid */}
      {!loading && !error && filteredExams.length > 0 && (
        <div className="grid grid-cols-1 gap-5 md:grid-cols-2 lg:grid-cols-3">
          {filteredExams.map((exam) => {
            const dateStr = exam.created_at
              ? new Date(exam.created_at).toLocaleDateString('en-IN', {
                  month: 'short',
                  day: 'numeric',
                  year: 'numeric',
                  hour: '2-digit',
                  minute: '2-digit',
                })
              : 'Recently Generated';

            const isDownloadingStudent = downloadingId === `${exam.id}-student`;
            const isDownloadingSolution = downloadingId === `${exam.id}-solution`;

            return (
              <div
                key={exam.id}
                className="flex flex-col justify-between rounded-xl border border-slate-200 bg-white p-5 shadow-sm transition hover:border-indigo-300 hover:shadow-md"
              >
                <div>
                  {/* Card Header */}
                  <div className="flex items-start justify-between gap-2">
                    <span className="inline-flex items-center rounded-md bg-indigo-50 px-2 py-1 text-xs font-bold text-indigo-700">
                      Class {exam.grade_level} • {exam.subject}
                    </span>
                    <button
                      onClick={(e) => handleDelete(exam.id, e)}
                      title="Delete saved paper"
                      className="rounded p-1 text-slate-400 transition hover:bg-red-50 hover:text-red-600"
                    >
                      <svg className="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                      </svg>
                    </button>
                  </div>

                  {/* Title */}
                  <h3 className="mt-2.5 text-base font-bold text-slate-900 line-clamp-2">
                    {exam.title}
                  </h3>

                  {/* Metadata Pills */}
                  <div className="mt-2.5 flex flex-wrap items-center gap-2 text-xs text-slate-600">
                    <span className="inline-flex items-center rounded bg-slate-100 px-2 py-0.5 font-semibold text-slate-700">
                      🎯 {exam.total_marks} Marks
                    </span>
                    <span className="inline-flex items-center rounded bg-slate-100 px-2 py-0.5 font-semibold text-slate-700">
                      ⏱️ {exam.duration_minutes} Mins
                    </span>
                    <span className="inline-flex items-center rounded bg-slate-100 px-2 py-0.5 font-semibold text-slate-700">
                      📝 {exam.question_ids?.length || 'Exam'} Questions
                    </span>
                  </div>

                  {/* Chapters List */}
                  {exam.selected_chapters && exam.selected_chapters.length > 0 && (
                    <div className="mt-3">
                      <span className="text-[11px] font-semibold uppercase tracking-wider text-slate-400">
                        Chapters:
                      </span>
                      <div className="mt-1 flex flex-wrap gap-1">
                        {exam.selected_chapters.slice(0, 3).map((ch, i) => (
                          <span
                            key={i}
                            className="rounded bg-slate-50 px-1.5 py-0.5 text-[11px] text-slate-600 border border-slate-200"
                          >
                            {ch}
                          </span>
                        ))}
                        {exam.selected_chapters.length > 3 && (
                          <span className="text-[11px] text-slate-400 self-center">
                            +{exam.selected_chapters.length - 3} more
                          </span>
                        )}
                      </div>
                    </div>
                  )}

                  {/* Date Created */}
                  <p className="mt-3 text-[11px] text-slate-400">{dateStr}</p>
                </div>

                {/* Actions */}
                <div className="mt-4 border-t border-slate-100 pt-3">
                  <div className="grid grid-cols-2 gap-2">
                    <button
                      onClick={() => handleDownload(exam.id, 'student', exam.title)}
                      disabled={isDownloadingStudent}
                      className="inline-flex items-center justify-center gap-1 rounded-lg border border-indigo-200 bg-indigo-50 px-2.5 py-1.5 text-xs font-semibold text-indigo-700 transition hover:bg-indigo-100 disabled:opacity-50"
                    >
                      {isDownloadingStudent ? '⏳ Building...' : '📥 Student Paper'}
                    </button>
                    <button
                      onClick={() => handleDownload(exam.id, 'solution', exam.title)}
                      disabled={isDownloadingSolution}
                      className="inline-flex items-center justify-center gap-1 rounded-lg border border-emerald-200 bg-emerald-50 px-2.5 py-1.5 text-xs font-semibold text-emerald-700 transition hover:bg-emerald-100 disabled:opacity-50"
                    >
                      {isDownloadingSolution ? '⏳ Building...' : '📋 Solutions'}
                    </button>
                  </div>

                  {onLoadExamToPreview && (
                    <button
                      onClick={() => onLoadExamToPreview(exam.id)}
                      className="mt-2 w-full text-center text-xs font-semibold text-slate-600 transition hover:text-indigo-600 py-1"
                    >
                      👁️ Open & Customize in Editor &#8594;
                    </button>
                  )}
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}
