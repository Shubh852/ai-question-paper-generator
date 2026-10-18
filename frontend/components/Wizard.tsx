'use client';

import React, { useState, useEffect } from 'react';
import {
  GraduationCap,
  BookOpen,
  Sliders,
  Eye,
  RefreshCw,
  Download,
  CheckCircle2,
  ChevronRight,
  ChevronLeft,
  Sparkles,
  Layers,
  Clock,
  Award,
  FileText,
  HelpCircle,
  BarChart3,
  CheckSquare,
  Square
} from 'lucide-react';
import LatexRenderer from './LatexRenderer';
import LeadCaptureModal from './LeadCaptureModal';

interface Topic {
  name: string;
  count: number;
}

interface Chapter {
  name: string;
  count: number;
  topics?: Topic[];
}

interface TaxonomyItem {
  grade: number;
  subjects: {
    subject: string;
    total_questions: number;
    chapters: Chapter[];
  }[];
}

interface Question {
  id: string;
  grade_level: number;
  subject: string;
  chapter: string;
  topic: string;
  primary_exam: string;
  difficulty_tier: number;
  question_format: string;
  marks: number;
  question_text_latex: string;
  options?: Record<string, string>;
  correct_option?: string;
  ideal_solution_latex: string;
  step_marking_rubric: { step: number; rule: string; allocated_marks: number }[];
  source_book?: string;
}

interface ExamPaper {
  id: string;
  title: string;
  grade_level: number;
  subject: string;
  total_marks: number;
  duration_minutes: number;
  exam_type: string;
  selected_chapters: string[];
  sections: Record<string, Question[]>;
  question_ids: string[];
  school_name?: string;
  school_logo?: string;
}

interface WizardProps {
  initialExam?: ExamPaper | null;
  onViewSavedPapers?: () => void;
  currentUser?: {
    id: string;
    name: string;
    school: string;
    city: string;
    email: string;
    whatsapp: string;
  } | null;
}

export default function Wizard({ initialExam, onViewSavedPapers, currentUser }: WizardProps = {}) {
  const [currentStep, setCurrentStep] = useState(1);
  const [taxonomy, setTaxonomy] = useState<TaxonomyItem[]>([]);
  const [loadingTaxonomy, setLoadingTaxonomy] = useState(true);

  // Step 1: Scope
  const [selectedGrade, setSelectedGrade] = useState<number>(10);
  const [selectedSubject, setSelectedSubject] = useState<string>('Mathematics');
  const [targetExam, setTargetExam] = useState<string>('CBSE_BOARD');

  // Step 2: Chapters & Topics
  const [selectedChapters, setSelectedChapters] = useState<string[]>([]);
  const [selectedTopics, setSelectedTopics] = useState<string[]>([]);
  const [expandedChapters, setExpandedChapters] = useState<string[]>([]);

  // Step 3: Blueprint & Branding
  const [totalMarks, setTotalMarks] = useState<number>(25);
  const [examTitle, setExamTitle] = useState<string>('Unit Assessment Test');
  const [difficulty, setDifficulty] = useState({ easy: 40, medium: 40, hard: 20 });
  const [schoolName, setSchoolName] = useState<string>(currentUser?.school || 'Delhi Public School');
  const [schoolLogoUrl, setSchoolLogoUrl] = useState<string>('/logos/default_school_logo.svg');
  const [uploadingLogo, setUploadingLogo] = useState(false);
  const logoInputRef = React.useRef<HTMLInputElement | null>(null);

  // Step 4: Preview
  const [examPaper, setExamPaper] = useState<ExamPaper | null>(null);
  const [generating, setGenerating] = useState(false);
  const [swappingId, setSwappingId] = useState<string | null>(null);
  const [activeSection, setActiveSection] = useState<string>('ALL');
  const [showMarkingScheme, setShowMarkingScheme] = useState(false);

  // Sync initialExam when loaded from Saved Papers
  useEffect(() => {
    if (initialExam) {
      setExamPaper(initialExam);
      if (initialExam.grade_level) setSelectedGrade(initialExam.grade_level);
      if (initialExam.subject) setSelectedSubject(initialExam.subject);
      if (initialExam.school_name) setSchoolName(initialExam.school_name);
      if (initialExam.school_logo) setSchoolLogoUrl(initialExam.school_logo);
      setCurrentStep(4);
    }
  }, [initialExam]);

  // Lead modal state
  const [isLeadModalOpen, setIsLeadModalOpen] = useState(false);
  const [pendingDocDownload, setPendingDocDownload] = useState<'student' | 'solution'>('student');
  const [isUnlocked, setIsUnlocked] = useState(false);

  const handleLogoUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;
    setUploadingLogo(true);
    try {
      const formData = new FormData();
      formData.append('file', file);
      const res = await fetch('/api/v1/upload-logo', {
        method: 'POST',
        body: formData,
      });
      if (!res.ok) throw new Error('Failed to upload logo');
      const data = await res.json();
      setSchoolLogoUrl(data.url);
    } catch (err: any) {
      alert(`Logo upload failed: ${err.message}`);
    } finally {
      setUploadingLogo(false);
    }
  };

  const toggleChapterExpand = (chapterName: string) => {
    setExpandedChapters((prev) =>
      prev.includes(chapterName) ? prev.filter((c) => c !== chapterName) : [...prev, chapterName]
    );
  };

  const toggleTopic = (topicName: string, chapterName: string) => {
    if (!selectedChapters.includes(chapterName)) {
      setSelectedChapters((prev) => [...prev, chapterName]);
    }
    setSelectedTopics((prev) =>
      prev.includes(topicName) ? prev.filter((t) => t !== topicName) : [...prev, topicName]
    );
  };

  // Fetch Taxonomy on mount
  useEffect(() => {
    async function fetchTaxonomy() {
      try {
        const res = await fetch('/api/v1/taxonomy');
        if (res.ok) {
          const data = await res.json();
          setTaxonomy(data.taxonomy || []);
        }
      } catch (e) {
        console.error('Failed to fetch taxonomy:', e);
      } finally {
        setLoadingTaxonomy(false);
      }
    }
    fetchTaxonomy();
  }, []);

  // Update available subjects and auto-select chapters when Grade changes
  const currentGradeData = taxonomy.find((t) => t.grade === selectedGrade);
  const availableSubjects = currentGradeData?.subjects || [];
  const currentSubjectData = availableSubjects.find(
    (s) => s.subject.toLowerCase() === selectedSubject.toLowerCase()
  );
  const availableChapters = currentSubjectData?.chapters || [];

  // When available chapters change, auto-select first chapter if none selected
  useEffect(() => {
    if (availableChapters.length > 0 && selectedChapters.length === 0) {
      setSelectedChapters([availableChapters[0].name]);
    }
  }, [availableChapters]);

  // Handle Generate Blueprint
  const handleGenerate = async (isRegenerating: boolean = false) => {
    const chaptersToUse = selectedChapters.length > 0 
      ? selectedChapters 
      : (examPaper?.selected_chapters || []);

    if (chaptersToUse.length === 0) {
      alert('Please select at least one chapter');
      return;
    }

    setGenerating(true);
    try {
      const res = await fetch('/api/v1/generate-blueprint', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          grade: selectedGrade,
          subject: selectedSubject,
          chapters: chaptersToUse,
          topics: selectedTopics.length > 0 ? selectedTopics : undefined,
          exam_type: targetExam,
          total_marks: totalMarks,
          difficulty: difficulty,
          title: examTitle || `Class ${selectedGrade} ${selectedSubject} Assessment`,
          school_name: schoolName,
          school_logo: schoolLogoUrl,
          exclude_question_ids: isRegenerating && examPaper?.question_ids ? examPaper.question_ids : undefined,
          created_by: currentUser?.name || undefined,
        }),
      });

      if (!res.ok) {
        const err = await res.json();
        throw new Error(err.detail || 'Failed to assemble exam paper');
      }

      const paper: ExamPaper = await res.json();
      paper.school_name = schoolName;
      paper.school_logo = schoolLogoUrl;
      setExamPaper(paper);
      setCurrentStep(4);
    } catch (e: any) {
      alert(`Error generating blueprint: ${e.message}`);
    } finally {
      setGenerating(false);
    }
  };

  // Handle Question Swap
  const handleSwap = async (currentQ: Question, sectionKey: string) => {
    if (!examPaper) return;
    setSwappingId(currentQ.id);

    try {
      const allCurrentIds = Object.values(examPaper.sections)
        .flat()
        .map((q) => q.id);

      const res = await fetch('/api/v1/swap-question', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          current_question_id: currentQ.id,
          excluded_ids: allCurrentIds,
        }),
      });

      if (!res.ok) {
        throw new Error('No equivalent question found to swap');
      }

      const data = await res.json();
      const newQuestion: Question = data.replacement;

      // Update question in examPaper state
      setExamPaper((prev) => {
        if (!prev) return prev;
        const newSections = { ...prev.sections };
        newSections[sectionKey] = newSections[sectionKey].map((q) =>
          q.id === currentQ.id ? newQuestion : q
        );
        return {
          ...prev,
          sections: newSections,
          question_ids: prev.question_ids.map((id) => (id === currentQ.id ? newQuestion.id : id)),
        };
      });
    } catch (e: any) {
      alert(e.message || 'Swap failed');
    } finally {
      setSwappingId(null);
    }
  };

  // Direct PDF Download
  const triggerPdfDownload = async (docType: 'student' | 'solution') => {
    if (!examPaper) return;

    try {
      const brandedExam = {
        ...examPaper,
        school_name: schoolName || examPaper.school_name,
        school_logo: schoolLogoUrl || examPaper.school_logo,
      };

      const res = await fetch('/api/v1/export-pdf', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          exam: brandedExam,
          target: docType,
        }),
      });

      if (!res.ok) {
        throw new Error('Failed to compile PDF');
      }

      const blob = await res.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `${docType === 'solution' ? 'Marking_Scheme' : 'Question_Paper'}_Class${selectedGrade}_${selectedSubject}.pdf`;
      document.body.appendChild(a);
      a.click();
      window.URL.revokeObjectURL(url);
      document.body.removeChild(a);
    } catch (e: any) {
      alert(`PDF download failed: ${e.message}`);
    }
  };

  const handleDownloadClick = (docType: 'student' | 'solution') => {
    if (isUnlocked) {
      triggerPdfDownload(docType);
    } else {
      setPendingDocDownload(docType);
      setIsLeadModalOpen(true);
    }
  };

  const steps = [
    { num: 1, label: 'Scope', icon: GraduationCap },
    { num: 2, label: 'Chapters', icon: BookOpen },
    { num: 3, label: 'Blueprint', icon: Sliders },
    { num: 4, label: 'Interactive IDE', icon: Eye },
  ];

  return (
    <div className="w-full max-w-7xl mx-auto px-4 py-8">
      {/* Stepper Header */}
      <div className="mb-8">
        <div className="flex items-center justify-between max-w-3xl mx-auto">
          {steps.map((s, idx) => {
            const Icon = s.icon;
            const isActive = currentStep === s.num;
            const isCompleted = currentStep > s.num;

            return (
              <React.Fragment key={s.num}>
                <button
                  onClick={() => s.num < currentStep && setCurrentStep(s.num)}
                  disabled={s.num > currentStep}
                  className={`flex items-center space-x-2 group focus:outline-none ${
                    s.num <= currentStep ? 'cursor-pointer' : 'cursor-not-allowed opacity-50'
                  }`}
                >
                  <div
                    className={`flex h-10 w-10 items-center justify-center rounded-xl font-bold transition-all ${
                      isActive
                        ? 'bg-blue-600 text-white shadow-lg shadow-blue-500/30 ring-4 ring-blue-100'
                        : isCompleted
                        ? 'bg-emerald-600 text-white'
                        : 'bg-slate-200 text-slate-600'
                    }`}
                  >
                    {isCompleted ? <CheckCircle2 className="h-5 w-5" /> : <Icon className="h-5 w-5" />}
                  </div>
                  <span
                    className={`text-sm font-semibold hidden sm:inline ${
                      isActive ? 'text-blue-600' : isCompleted ? 'text-emerald-700' : 'text-slate-500'
                    }`}
                  >
                    {s.label}
                  </span>
                </button>
                {idx < steps.length - 1 && (
                  <div
                    className={`h-0.5 flex-1 mx-3 transition-colors ${
                      currentStep > idx + 1 ? 'bg-emerald-500' : 'bg-slate-200'
                    }`}
                  />
                )}
              </React.Fragment>
            );
          })}
        </div>
      </div>

      {/* STEP 1: SCOPE */}
      {currentStep === 1 && (
        <div className="bg-white rounded-3xl p-6 sm:p-10 shadow-xl border border-slate-100 max-w-3xl mx-auto animate-in fade-in">
          <div className="mb-8">
            <h2 className="text-2xl font-black text-slate-900 tracking-tight">Select Exam Scope</h2>
            <p className="text-sm text-slate-500 mt-1">
              Choose your target grade, curriculum subject, and examination format standard.
            </p>
          </div>

          <div className="space-y-6">
            {/* Grade Selection */}
            <div>
              <label className="block text-xs font-bold uppercase tracking-wider text-slate-500 mb-2">
                1. Target Class / Grade Level
              </label>
              <div className="grid grid-cols-3 gap-3">
                {[10, 11, 12].map((g) => (
                  <button
                    key={g}
                    onClick={() => {
                      setSelectedGrade(g);
                      if (g === 10) setSelectedSubject('Mathematics');
                      else setSelectedSubject('Physics');
                      setSelectedChapters([]);
                      setSelectedTopics([]);
                      setExpandedChapters([]);
                    }}
                    className={`flex flex-col items-center justify-center p-4 rounded-2xl border-2 transition-all ${
                      selectedGrade === g
                        ? 'border-blue-600 bg-blue-50/60 text-blue-900 shadow-md'
                        : 'border-slate-200 hover:border-slate-300 text-slate-700'
                    }`}
                  >
                    <span className="text-2xl font-black">Class {g}</span>
                    <span className="text-[11px] font-medium text-slate-500 mt-0.5">
                      {g === 10 ? 'CBSE Secondary' : 'Senior Secondary'}
                    </span>
                  </button>
                ))}
              </div>
            </div>

            {/* Subject Selection */}
            <div>
              <label className="block text-xs font-bold uppercase tracking-wider text-slate-500 mb-2">
                2. Curriculum Subject
              </label>
              <div className="grid grid-cols-2 sm:grid-cols-3 gap-3">
                {availableSubjects.map((s) => (
                  <button
                    key={s.subject}
                    onClick={() => {
                      setSelectedSubject(s.subject);
                      setSelectedChapters([]);
                      setSelectedTopics([]);
                      setExpandedChapters([]);
                    }}
                    className={`flex items-center justify-between p-3.5 rounded-xl border text-left transition-all ${
                      selectedSubject.toLowerCase() === s.subject.toLowerCase()
                        ? 'border-blue-600 bg-blue-50/70 text-blue-900 font-bold ring-1 ring-blue-500'
                        : 'border-slate-200 hover:border-slate-300 text-slate-700'
                    }`}
                  >
                    <span className="text-sm">{s.subject}</span>
                    <span className="text-[10px] bg-white/80 px-2 py-0.5 rounded-full border border-slate-200 text-slate-500">
                      {s.total_questions} Qs
                    </span>
                  </button>
                ))}
              </div>
            </div>

            {/* Target Exam */}
            <div>
              <label className="block text-xs font-bold uppercase tracking-wider text-slate-500 mb-2">
                3. Examination Target Standard
              </label>
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
                {[
                  {
                    id: 'CBSE_BOARD',
                    title: 'CBSE Board Standard',
                    desc: 'Strict NCERT blueprint, Section A-E structure, step rubrics',
                  },
                  {
                    id: 'JEE_MAIN',
                    title: 'IIT-JEE / NEET',
                    desc: 'Higher cognitive difficulty, multi-concept problems',
                  },
                  {
                    id: 'HYBRID',
                    title: 'Hybrid Foundation',
                    desc: '60% NCERT Core + 40% Competitive application',
                  },
                ].map((item) => (
                  <button
                    key={item.id}
                    onClick={() => setTargetExam(item.id)}
                    className={`p-4 rounded-xl border-2 text-left transition-all ${
                      targetExam === item.id
                        ? 'border-blue-600 bg-blue-50/60 shadow-sm'
                        : 'border-slate-200 hover:border-slate-300'
                    }`}
                  >
                    <div className="font-bold text-sm text-slate-900">{item.title}</div>
                    <div className="text-xs text-slate-500 mt-1 leading-relaxed">{item.desc}</div>
                  </button>
                ))}
              </div>
            </div>
          </div>

          <div className="mt-8 flex justify-end">
            <button
              onClick={() => setCurrentStep(2)}
              className="flex items-center space-x-2 rounded-xl bg-blue-600 px-6 py-3 text-sm font-bold text-white shadow-md hover:bg-blue-700 transition-all active:scale-[0.99]"
            >
              <span>Next: Select Chapters</span>
              <ChevronRight className="h-4 w-4" />
            </button>
          </div>
        </div>
      )}

      {/* STEP 2: CHAPTER SELECTION */}
      {currentStep === 2 && (
        <div className="bg-white rounded-3xl p-6 sm:p-10 shadow-xl border border-slate-100 max-w-3xl mx-auto animate-in fade-in">
          <div className="flex items-center justify-between mb-6">
            <div>
              <h2 className="text-2xl font-black text-slate-900 tracking-tight">Select Syllabus Chapters</h2>
              <p className="text-sm text-slate-500 mt-1">
                Class {selectedGrade} • {selectedSubject} — Choose one or more chapters for paper generation.
              </p>
            </div>
            <button
              onClick={() => {
                if (selectedChapters.length === availableChapters.length) {
                  setSelectedChapters([]);
                } else {
                  setSelectedChapters(availableChapters.map((c) => c.name));
                }
              }}
              className="text-xs font-semibold text-blue-600 hover:text-blue-800 transition-colors"
            >
              {selectedChapters.length === availableChapters.length ? 'Deselect All' : 'Select All Chapters'}
            </button>
          </div>

          <div className="space-y-3 max-h-[460px] overflow-y-auto pr-1">
            {availableChapters.map((ch, idx) => {
              const isSelected = selectedChapters.includes(ch.name);
              const isExpanded = expandedChapters.includes(ch.name);
              const chapterTopics = ch.topics || [];
              const selectedTopicCountInChapter = chapterTopics.filter((t) =>
                selectedTopics.includes(t.name)
              ).length;

              return (
                <div
                  key={ch.name}
                  className={`rounded-2xl border-2 transition-all overflow-hidden ${
                    isSelected
                      ? 'border-blue-600 bg-blue-50/30 shadow-sm'
                      : 'border-slate-200 hover:border-slate-300 bg-white'
                  }`}
                >
                  <div
                    onClick={() => {
                      if (isSelected) {
                        setSelectedChapters(selectedChapters.filter((c) => c !== ch.name));
                        if (chapterTopics.length > 0) {
                          const topicNames = chapterTopics.map((t) => t.name);
                          setSelectedTopics(selectedTopics.filter((t) => !topicNames.includes(t)));
                        }
                      } else {
                        setSelectedChapters([...selectedChapters, ch.name]);
                      }
                    }}
                    className="flex items-center justify-between p-4 cursor-pointer select-none"
                  >
                    <div className="flex items-center space-x-3">
                      {isSelected ? (
                        <CheckSquare className="h-5 w-5 text-blue-600 flex-shrink-0" />
                      ) : (
                        <Square className="h-5 w-5 text-slate-400 flex-shrink-0" />
                      )}
                      <div>
                        <span className="text-sm font-bold text-slate-900">
                          {idx + 1}. {ch.name}
                        </span>
                        {selectedTopicCountInChapter > 0 && (
                          <span className="ml-2 inline-flex items-center text-[10px] bg-blue-100 text-blue-800 font-bold px-2 py-0.5 rounded-full">
                            {selectedTopicCountInChapter} topics selected
                          </span>
                        )}
                      </div>
                    </div>
                    <div className="flex items-center space-x-2">
                      <span className="text-xs font-medium text-slate-500 bg-white px-2.5 py-1 rounded-full border border-slate-200 shadow-xs">
                        {ch.count} Qs
                      </span>
                      {chapterTopics.length > 0 && (
                        <button
                          type="button"
                          onClick={(e) => {
                            e.stopPropagation();
                            toggleChapterExpand(ch.name);
                          }}
                          className={`text-xs px-2.5 py-1 rounded-lg border font-semibold transition-all ${
                            isExpanded
                              ? 'bg-blue-600 text-white border-blue-600 shadow-xs'
                              : 'bg-white text-blue-600 border-blue-200 hover:bg-blue-50'
                          }`}
                        >
                          {isExpanded ? 'Hide Topics ▴' : `${chapterTopics.length} Topics ▾`}
                        </button>
                      )}
                    </div>
                  </div>

                  {/* Expandable Topic Selection Pills */}
                  {isExpanded && chapterTopics.length > 0 && (
                    <div className="px-4 pb-3.5 pt-2 border-t border-blue-100 bg-slate-50/70">
                      <div className="flex items-center justify-between mb-2">
                        <span className="text-[11px] font-bold uppercase tracking-wider text-slate-500">
                          Filter by Specific Topics:
                        </span>
                        <button
                          type="button"
                          onClick={(e) => {
                            e.stopPropagation();
                            const topicNames = chapterTopics.map((t) => t.name);
                            const allSelected = topicNames.every((t) => selectedTopics.includes(t));
                            if (allSelected) {
                              setSelectedTopics(selectedTopics.filter((t) => !topicNames.includes(t)));
                            } else {
                              if (!selectedChapters.includes(ch.name)) {
                                setSelectedChapters([...selectedChapters, ch.name]);
                              }
                              setSelectedTopics(Array.from(new Set([...selectedTopics, ...topicNames])));
                            }
                          }}
                          className="text-[11px] font-bold text-blue-600 hover:text-blue-800"
                        >
                          {chapterTopics.every((t) => selectedTopics.includes(t.name))
                            ? 'Clear Topics'
                            : 'Select All Topics'}
                        </button>
                      </div>
                      <div className="flex flex-wrap gap-1.5">
                        {chapterTopics.map((t) => {
                          const isTopicSelected = selectedTopics.includes(t.name);
                          return (
                            <button
                              key={t.name}
                              type="button"
                              onClick={(e) => {
                                e.stopPropagation();
                                toggleTopic(t.name, ch.name);
                              }}
                              className={`text-xs px-3 py-1.5 rounded-xl border transition-all flex items-center space-x-1.5 ${
                                isTopicSelected
                                  ? 'bg-blue-600 text-white border-blue-600 font-semibold shadow-xs'
                                  : 'bg-white text-slate-700 border-slate-200 hover:border-slate-300 hover:bg-slate-100'
                              }`}
                            >
                              <span>{t.name}</span>
                              <span
                                className={`text-[10px] px-1.5 py-0.5 rounded-full font-bold ${
                                  isTopicSelected
                                    ? 'bg-blue-700 text-blue-100'
                                    : 'bg-slate-100 text-slate-500'
                                }`}
                              >
                                {t.count}
                              </span>
                            </button>
                          );
                        })}
                      </div>
                    </div>
                  )}
                </div>
              );
            })}
          </div>

          <div className="mt-8 flex items-center justify-between pt-4 border-t border-slate-100">
            <button
              onClick={() => setCurrentStep(1)}
              className="flex items-center space-x-1.5 text-sm font-semibold text-slate-600 hover:text-slate-900"
            >
              <ChevronLeft className="h-4 w-4" />
              <span>Back</span>
            </button>
            <button
              onClick={() => setCurrentStep(3)}
              disabled={selectedChapters.length === 0}
              className="flex items-center space-x-2 rounded-xl bg-blue-600 px-6 py-3 text-sm font-bold text-white shadow-md hover:bg-blue-700 transition-all disabled:opacity-50"
            >
              <span>Next: Configure Blueprint ({selectedChapters.length} Selected)</span>
              <ChevronRight className="h-4 w-4" />
            </button>
          </div>
        </div>
      )}

      {/* STEP 3: BLUEPRINT & PRESETS */}
      {currentStep === 3 && (
        <div className="bg-white rounded-3xl p-6 sm:p-10 shadow-xl border border-slate-100 max-w-3xl mx-auto animate-in fade-in">
          <div className="mb-6">
            <h2 className="text-2xl font-black text-slate-900 tracking-tight">Exam Blueprint Configuration</h2>
            <p className="text-sm text-slate-500 mt-1">
              Select standard CBSE marks distribution or customize time and difficulty tiers.
            </p>
          </div>

          <div className="space-y-6">
            {/* Presets */}
            <div>
              <div className="flex items-center justify-between mb-2">
                <label className="block text-xs font-bold uppercase tracking-wider text-slate-500">
                  Exam Format & Pattern Presets
                </label>
                <span className="text-xs font-semibold text-blue-600">
                  Selected: {totalMarks} Marks
                </span>
              </div>
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
                {[
                  {
                    marks: 15,
                    title: 'Class Test / Weekly Quiz',
                    time: '35 Mins',
                    structure: '5 MCQs (5M) + 2 SA-I (4M) + 2 SA-II (6M)',
                    tag: 'Popular',
                  },
                  {
                    marks: 20,
                    title: 'Periodic Test I',
                    time: '45 Mins',
                    structure: '6 MCQs (6M) + 4 SA-I (8M) + 2 SA-II (6M)',
                  },
                  {
                    marks: 25,
                    title: 'Unit Assessment Test',
                    time: '1 Hour',
                    structure: '5 MCQs (5M) + 3 SA-I (6M) + 3 SA-II (9M) + 1 LA (5M)',
                  },
                  {
                    marks: 40,
                    title: 'Periodic Assessment II',
                    time: '1.5 Hours',
                    structure: '10 MCQs (10M) + 4 SA-I (8M) + 4 SA-II (12M) + 2 LA (10M)',
                  },
                  {
                    marks: 50,
                    title: 'Mid-Term Examination',
                    time: '2 Hours',
                    structure: '12 MCQs (12M) + 5 SA-I (10M) + 6 SA-II (18M) + 2 LA (10M)',
                  },
                  {
                    marks: 70,
                    title: 'CBSE Science Theory',
                    time: '3 Hours',
                    structure: '16 MCQs (16M) + 5 SA (10M) + 7 SA (21M) + 2 Case (8M) + 3 LA (15M)',
                    tag: 'Board Science',
                  },
                  {
                    marks: 80,
                    title: 'CBSE Full Board Exam',
                    time: '3 Hours',
                    structure: '20 MCQs (20M) + 5 SA (10M) + 6 SA (18M) + 4 LA (20M) + 3 Case (12M)',
                    tag: 'Board Standard',
                  },
                ].map((p) => (
                  <button
                    key={p.marks}
                    type="button"
                    onClick={() => {
                      setTotalMarks(p.marks);
                      setExamTitle(`Class ${selectedGrade} ${selectedSubject} ${p.title}`);
                    }}
                    className={`p-3.5 rounded-2xl border-2 text-left transition-all relative ${
                      totalMarks === p.marks
                        ? 'border-blue-600 bg-blue-50/70 shadow-md ring-1 ring-blue-500'
                        : 'border-slate-200 hover:border-slate-300 bg-white'
                    }`}
                  >
                    {p.tag && (
                      <span className="absolute -top-2.5 right-3 text-[10px] font-black uppercase tracking-wider bg-blue-600 text-white px-2 py-0.5 rounded-full shadow-xs">
                        {p.tag}
                      </span>
                    )}
                    <div className="flex items-center justify-between">
                      <span className="text-base font-black text-slate-900">{p.marks} Marks</span>
                      <span className="text-[11px] font-semibold bg-blue-100 text-blue-800 px-2 py-0.5 rounded-full">
                        {p.time}
                      </span>
                    </div>
                    <div className="font-bold text-xs text-slate-800 mt-1.5">{p.title}</div>
                    <div className="text-[11px] text-slate-500 mt-1 leading-snug">{p.structure}</div>
                  </button>
                ))}
              </div>

              {/* Custom Marks Input */}
              <div className="mt-4 p-4 rounded-2xl border border-slate-200 bg-slate-50/70">
                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                  <div>
                    <span className="text-xs font-bold text-slate-700">Custom Marks Pattern:</span>
                    <p className="text-[11px] text-slate-500 mt-0.5">
                      Enter any mark count. Our AI solver will automatically partition the sections.
                    </p>
                  </div>
                  <div className="flex items-center space-x-2">
                    <input
                      type="number"
                      min={5}
                      max={100}
                      value={totalMarks}
                      onChange={(e) => {
                        const val = parseInt(e.target.value) || 15;
                        setTotalMarks(val);
                        setExamTitle(`Class ${selectedGrade} ${selectedSubject} Assessment (${val} Marks)`);
                      }}
                      className="w-20 rounded-xl border border-slate-300 bg-white px-3 py-1.5 text-center text-sm font-bold text-slate-900 focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500"
                    />
                    <span className="text-xs font-bold text-slate-600">Marks</span>
                  </div>
                </div>

                <div className="flex flex-wrap items-center gap-1.5 mt-3 pt-3 border-t border-slate-200">
                  <span className="text-[11px] font-bold text-slate-500 mr-1">Quick Select:</span>
                  {[10, 15, 20, 25, 30, 40, 50, 70, 80, 100].map((m) => (
                    <button
                      key={m}
                      type="button"
                      onClick={() => {
                        setTotalMarks(m);
                        setExamTitle(`Class ${selectedGrade} ${selectedSubject} Assessment (${m} Marks)`);
                      }}
                      className={`px-2.5 py-1 rounded-lg text-xs font-bold transition-all ${
                        totalMarks === m
                          ? 'bg-blue-600 text-white shadow-xs'
                          : 'bg-white text-slate-700 border border-slate-200 hover:bg-slate-100'
                      }`}
                    >
                      {m}M
                    </button>
                  ))}
                </div>
              </div>
            </div>

            {/* Custom Exam Title */}
            <div>
              <label className="block text-xs font-bold uppercase tracking-wider text-slate-500 mb-1">
                Examination Paper Title
              </label>
              <input
                type="text"
                value={examTitle}
                onChange={(e) => setExamTitle(e.target.value)}
                placeholder="e.g. Periodic Assessment Test - Unit 1"
                className="w-full rounded-xl border border-slate-300 px-3.5 py-2.5 text-sm focus:border-blue-500 focus:outline-none focus:ring-1 focus:ring-blue-500"
              />
            </div>

            {/* School Branding & Logo Customization */}
            <div className="rounded-2xl border border-indigo-100 bg-indigo-50/50 p-4">
              <div className="flex items-center justify-between mb-2">
                <label className="block text-xs font-bold uppercase tracking-wider text-indigo-900">
                  School Branding & Header Emblem
                </label>
                <span className="text-[11px] font-semibold text-indigo-700 bg-indigo-100 px-2 py-0.5 rounded-full">
                  Appears on PDF Prints
                </span>
              </div>
              <p className="text-xs text-slate-500 mb-3">
                Customize the school name and crest emblem to generate official branded question papers and marking schemes.
              </p>

              <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
                <div className="sm:col-span-2">
                  <label className="block text-[11px] font-bold text-slate-700 mb-1">
                    School / Institution Name:
                  </label>
                  <input
                    type="text"
                    value={schoolName}
                    onChange={(e) => setSchoolName(e.target.value)}
                    placeholder="e.g. Delhi Public School, R.K. Puram"
                    className="w-full rounded-xl border border-slate-300 bg-white px-3.5 py-2 text-sm text-slate-900 focus:border-indigo-500 focus:outline-none focus:ring-1 focus:ring-indigo-500"
                  />
                </div>

                <div>
                  <label className="block text-[11px] font-bold text-slate-700 mb-1">
                    School Crest / Logo:
                  </label>
                  <div className="flex items-center space-x-2">
                    <div className="h-10 w-10 rounded-lg border border-slate-200 bg-white p-1 flex items-center justify-center flex-shrink-0 shadow-xs">
                      {schoolLogoUrl ? (
                        <img src={schoolLogoUrl} alt="Logo" className="h-full w-full object-contain" />
                      ) : (
                        <Award className="h-5 w-5 text-indigo-600" />
                      )}
                    </div>
                    <input
                      type="file"
                      ref={logoInputRef}
                      onChange={handleLogoUpload}
                      accept="image/*"
                      className="hidden"
                    />
                    <button
                      type="button"
                      onClick={() => logoInputRef.current?.click()}
                      disabled={uploadingLogo}
                      className="flex-1 rounded-xl border border-slate-300 bg-white px-2.5 py-2 text-xs font-semibold text-slate-700 hover:bg-slate-50 shadow-xs transition"
                    >
                      {uploadingLogo ? 'Uploading...' : 'Upload Logo'}
                    </button>
                    {schoolLogoUrl !== '/logos/default_school_logo.svg' && (
                      <button
                        type="button"
                        onClick={() => setSchoolLogoUrl('/logos/default_school_logo.svg')}
                        title="Reset to default emblem"
                        className="rounded-lg border border-slate-200 bg-white p-2 text-xs text-slate-400 hover:text-slate-600"
                      >
                        ✕
                      </button>
                    )}
                  </div>
                </div>
              </div>
            </div>

            {/* Difficulty Breakdown */}
            <div className="rounded-2xl border border-slate-200 p-4 bg-slate-50/60">
              <label className="block text-xs font-bold uppercase tracking-wider text-slate-600 mb-3 flex items-center justify-between">
                <span>Cognitive Difficulty Distribution</span>
                <span className="text-blue-600 font-normal normal-case">
                  Easy: {difficulty.easy}% • Medium: {difficulty.medium}% • Hard: {difficulty.hard}%
                </span>
              </label>
              <div className="h-3 w-full rounded-full bg-slate-200 overflow-hidden flex">
                <div style={{ width: `${difficulty.easy}%` }} className="bg-emerald-500" title="Easy" />
                <div style={{ width: `${difficulty.medium}%` }} className="bg-amber-500" title="Medium" />
                <div style={{ width: `${difficulty.hard}%` }} className="bg-rose-500" title="Hard" />
              </div>
              <div className="flex justify-between text-[11px] text-slate-500 mt-2">
                <span className="flex items-center space-x-1">
                  <span className="h-2 w-2 rounded-full bg-emerald-500" />
                  <span>NCERT Direct Recall</span>
                </span>
                <span className="flex items-center space-x-1">
                  <span className="h-2 w-2 rounded-full bg-amber-500" />
                  <span>Conceptual Understanding</span>
                </span>
                <span className="flex items-center space-x-1">
                  <span className="h-2 w-2 rounded-full bg-rose-500" />
                  <span>HOTS & Numerical Application</span>
                </span>
              </div>
            </div>
          </div>

          <div className="mt-8 flex items-center justify-between pt-4 border-t border-slate-100">
            <button
              onClick={() => setCurrentStep(2)}
              className="flex items-center space-x-1.5 text-sm font-semibold text-slate-600 hover:text-slate-900"
            >
              <ChevronLeft className="h-4 w-4" />
              <span>Back</span>
            </button>
            <button
              onClick={handleGenerate}
              disabled={generating}
              className="flex items-center space-x-2 rounded-xl bg-blue-600 px-7 py-3.5 text-sm font-bold text-white shadow-lg shadow-blue-500/25 hover:bg-blue-700 active:scale-[0.99] transition-all disabled:opacity-50"
            >
              {generating ? (
                <>
                  <RefreshCw className="h-4 w-4 animate-spin" />
                  <span>Assembling Question Paper...</span>
                </>
              ) : (
                <>
                  <Sparkles className="h-4 w-4" />
                  <span>Generate Paper & Preview</span>
                </>
              )}
            </button>
          </div>
        </div>
      )}

      {/* STEP 4: INTERACTIVE IDE & PREVIEW */}
      {currentStep === 4 && examPaper && (
        <div className="animate-in fade-in space-y-6">
          {/* Top Action Bar */}
          <div className="bg-white rounded-2xl p-4 shadow-md border border-slate-200 flex flex-wrap items-center justify-between gap-4">
            <div className="flex items-center space-x-3">
              <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-blue-100 text-blue-700 font-black">
                {examPaper.grade_level}
              </div>
              <div>
                <h2 className="font-extrabold text-base text-slate-900">{examPaper.title}</h2>
                <div className="flex items-center space-x-2 text-xs text-slate-500">
                  <span>{examPaper.subject}</span>
                  <span>•</span>
                  <span>{examPaper.total_marks} Marks</span>
                  <span>•</span>
                  <span>{examPaper.duration_minutes} Mins</span>
                </div>
              </div>
            </div>

            <div className="flex flex-wrap items-center gap-2.5">
              <button
                onClick={() => handleGenerate(true)}
                disabled={generating}
                className="flex items-center space-x-1.5 rounded-xl bg-purple-600 px-3.5 py-2 text-xs font-bold text-white shadow-sm hover:bg-purple-700 transition-all disabled:opacity-50"
                title="Shuffle and draw a fresh combination of questions adhering to this blueprint"
              >
                <RefreshCw className={`h-3.5 w-3.5 ${generating ? 'animate-spin' : ''}`} />
                <span>{generating ? 'Regenerating...' : 'Regenerate Entire Paper'}</span>
              </button>

              <button
                onClick={() => setShowMarkingScheme(!showMarkingScheme)}
                className={`flex items-center space-x-1.5 rounded-xl px-3.5 py-2 text-xs font-bold transition-all border ${
                  showMarkingScheme
                    ? 'bg-amber-100 text-amber-900 border-amber-300'
                    : 'bg-slate-100 text-slate-700 border-slate-200 hover:bg-slate-200'
                }`}
              >
                <HelpCircle className="h-3.5 w-3.5" />
                <span>{showMarkingScheme ? 'Hide Marking Scheme' : 'View Marking Scheme'}</span>
              </button>

              <button
                onClick={() => handleDownloadClick('student')}
                className="flex items-center space-x-1.5 rounded-xl bg-blue-600 px-4 py-2 text-xs font-bold text-white shadow-sm hover:bg-blue-700 transition-all"
              >
                <Download className="h-3.5 w-3.5" />
                <span>Question Paper (PDF)</span>
              </button>

              <button
                onClick={() => handleDownloadClick('solution')}
                className="flex items-center space-x-1.5 rounded-xl bg-emerald-600 px-4 py-2 text-xs font-bold text-white shadow-sm hover:bg-emerald-700 transition-all"
              >
                <Download className="h-3.5 w-3.5" />
                <span>Marking Scheme (PDF)</span>
              </button>

              <button
                onClick={() => setCurrentStep(3)}
                className="rounded-xl border border-slate-300 px-3 py-2 text-xs font-semibold text-slate-600 hover:bg-slate-50"
              >
                Reconfigure
              </button>
            </div>
          </div>

          {/* Split-Panel IDE Layout */}
          <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">
            {/* Left Section Navigation Panel */}
            <div className="lg:col-span-1 space-y-3">
              <div className="bg-white rounded-2xl p-4 shadow-sm border border-slate-200">
                <h3 className="text-xs font-black uppercase tracking-wider text-slate-500 mb-3">
                  Sections & Breakdown
                </h3>
                <div className="space-y-1.5">
                  <button
                    onClick={() => setActiveSection('ALL')}
                    className={`w-full flex items-center justify-between px-3 py-2 rounded-xl text-xs font-semibold transition-all ${
                      activeSection === 'ALL'
                        ? 'bg-blue-600 text-white font-bold shadow-sm'
                        : 'text-slate-600 hover:bg-slate-100'
                    }`}
                  >
                    <span>All Sections</span>
                    <span className="text-[10px] bg-black/10 px-1.5 py-0.5 rounded-full">
                      {Object.values(examPaper.sections).flat().length} Qs
                    </span>
                  </button>

                  {Object.entries(examPaper.sections).map(([secKey, qList]) => {
                    const secMarks = qList.reduce((acc, q) => acc + q.marks, 0);
                    return (
                      <button
                        key={secKey}
                        onClick={() => setActiveSection(secKey)}
                        className={`w-full flex items-center justify-between px-3 py-2 rounded-xl text-xs font-semibold transition-all ${
                          activeSection === secKey
                            ? 'bg-blue-600 text-white font-bold shadow-sm'
                            : 'text-slate-600 hover:bg-slate-100'
                        }`}
                      >
                        <span>Section {secKey}</span>
                        <div className="flex items-center space-x-1.5 text-[10px]">
                          <span className="opacity-80">{qList.length} Qs</span>
                          <span>•</span>
                          <span className="font-bold">{secMarks}M</span>
                        </div>
                      </button>
                    );
                  })}
                </div>
              </div>

              {/* Syllabus Info Card */}
              <div className="bg-gradient-to-br from-slate-900 to-slate-800 rounded-2xl p-4 text-white shadow-md">
                <div className="text-[11px] font-bold uppercase tracking-wider text-blue-400">
                  Target Coverage
                </div>
                <div className="mt-2 space-y-1 text-xs text-slate-300">
                  {examPaper.selected_chapters.map((ch, idx) => (
                    <div key={idx} className="flex items-center space-x-1.5">
                      <span className="h-1.5 w-1.5 rounded-full bg-blue-400" />
                      <span className="truncate">{ch}</span>
                    </div>
                  ))}
                </div>
              </div>
            </div>

            {/* Center Document Review IDE */}
            <div className="lg:col-span-3 bg-white rounded-3xl p-6 sm:p-10 shadow-lg border border-slate-200 min-h-[700px]">
              {/* Paper CBSE Layout Header with School Branding */}
              <div className="pb-6 border-b-2 border-slate-900 mb-6">
                <div className="flex items-center justify-between gap-4">
                  {schoolLogoUrl && (
                    <div className="h-14 w-14 flex-shrink-0 flex items-center justify-center">
                      <img src={schoolLogoUrl} alt="School Crest" className="max-h-full max-w-full object-contain" />
                    </div>
                  )}
                  <div className="text-center flex-1">
                    <div className="text-sm font-black text-slate-900 uppercase tracking-wide">
                      {schoolName ? schoolName.toUpperCase() : 'CENTRAL BOARD OF SECONDARY EDUCATION'}
                    </div>
                    <div className="text-[10px] font-bold text-slate-500 uppercase tracking-wider">
                      AFFILIATED TO CBSE, NEW DELHI
                    </div>
                    <h1 className="text-lg sm:text-xl font-black text-slate-900 mt-1 uppercase tracking-tight">
                      {examPaper.title}
                    </h1>
                    <div className="text-xs font-bold text-slate-700 mt-0.5">
                      CLASS {examPaper.grade_level} — {examPaper.subject.toUpperCase()}
                    </div>
                  </div>
                  {schoolLogoUrl && (
                    <div className="h-14 w-14 flex-shrink-0 flex items-center justify-center">
                      <img src={schoolLogoUrl} alt="School Crest" className="max-h-full max-w-full object-contain" />
                    </div>
                  )}
                </div>
                <div className="mt-4 flex items-center justify-between text-xs font-bold text-slate-700 border-t border-slate-300 pt-2 px-1">
                  <span>Time Allowed: {Math.floor(examPaper.duration_minutes / 60)} Hours {examPaper.duration_minutes % 60 > 0 ? `${examPaper.duration_minutes % 60} Mins` : ''}</span>
                  <span>Maximum Marks: {examPaper.total_marks}</span>
                </div>
              </div>

              {/* General Instructions Box */}
              <div className="rounded-xl bg-slate-50 p-4 border border-slate-200 text-xs text-slate-600 mb-8 leading-relaxed">
                <div className="font-bold text-slate-900 mb-1">General Instructions:</div>
                <ol className="list-decimal pl-4 space-y-0.5">
                  <li>This question paper contains 5 Sections: A, B, C, D, and E.</li>
                  <li>Section A comprises MCQs and Assertion-Reason questions of 1 mark each.</li>
                  <li>Section B comprises Very Short Answer (VSA) questions of 2 marks each.</li>
                  <li>Section C comprises Short Answer (SA) questions of 3 marks each.</li>
                  <li>Section D comprises Long Answer (LA) questions of 5 marks each.</li>
                  <li>Section E comprises Case Based integrated units of assessment of 4 marks each.</li>
                </ol>
              </div>

              {/* Sections Display */}
              {Object.entries(examPaper.sections)
                .filter(([secKey]) => activeSection === 'ALL' || activeSection === secKey)
                .map(([secKey, questions]) => {
                  return (
                    <div key={secKey} className="mb-10">
                      <div className="text-center my-6">
                        <span className="inline-block bg-blue-50 text-blue-900 text-xs font-black px-4 py-1.5 rounded-full border border-blue-200 uppercase tracking-wider">
                          SECTION {secKey}
                        </span>
                      </div>

                      <div className="space-y-6">
                        {questions.map((q, idx) => {
                          const isSwapping = swappingId === q.id;

                          return (
                            <div
                              key={q.id}
                              className={`group relative p-4 rounded-2xl border transition-all ${
                                isSwapping
                                  ? 'bg-amber-50/50 border-amber-300 animate-pulse'
                                  : 'bg-white border-slate-200 hover:border-blue-400 hover:shadow-sm'
                              }`}
                            >
                              <div className="flex items-start justify-between gap-4">
                                <div className="flex-1">
                                  <div className="flex items-center space-x-2 text-xs font-bold text-slate-400 mb-1.5 flex-wrap gap-y-1">
                                    <span className="text-slate-900 text-sm">Q{idx + 1}.</span>
                                    <span className="text-slate-600">({q.chapter} • {q.topic})</span>
                                    {q.source_book && (
                                      <span className="inline-flex items-center rounded-md bg-purple-50 px-2 py-0.5 text-[10px] font-semibold text-purple-700 border border-purple-200">
                                        📖 {q.source_book}
                                      </span>
                                    )}
                                  </div>

                                  <div className="text-sm font-medium text-slate-900 leading-relaxed">
                                    <LatexRenderer text={q.question_text_latex} />
                                  </div>

                                  {/* MCQ Options */}
                                  {q.options && typeof q.options === 'object' && (
                                    <div className="mt-3 grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
                                      {Object.entries(q.options).map(([optKey, optVal]) => (
                                        <div
                                          key={optKey}
                                          className="flex items-start space-x-2 p-2 rounded-lg bg-slate-50 border border-slate-200"
                                        >
                                          <span className="font-bold text-slate-700">({optKey})</span>
                                          <LatexRenderer text={String(optVal)} />
                                        </div>
                                      ))}
                                    </div>
                                  )}

                                  {/* Step-Wise Model Solution (if toggled) */}
                                  {showMarkingScheme && (
                                    <div className="mt-4 rounded-xl bg-emerald-50/70 border border-emerald-200 p-3.5 text-xs">
                                      <div className="font-bold text-emerald-900 mb-1 flex items-center space-x-1.5">
                                        <CheckCircle2 className="h-3.5 w-3.5 text-emerald-600" />
                                        <span>Model Solution & Evaluation Rubric:</span>
                                      </div>
                                      {q.correct_option && (
                                        <div className="font-bold text-emerald-700 mb-2">
                                          Correct Option: ({q.correct_option})
                                        </div>
                                      )}
                                      <div className="text-slate-800 mb-3">
                                        <LatexRenderer text={q.ideal_solution_latex} />
                                      </div>

                                      {/* Rubric Breakdown */}
                                      {q.step_marking_rubric && q.step_marking_rubric.length > 0 && (
                                        <div className="overflow-x-auto">
                                          <table className="w-full text-left text-[11px] border border-emerald-200 rounded-lg">
                                            <thead className="bg-emerald-100/60 font-bold text-emerald-900">
                                              <tr>
                                                <th className="p-1.5 w-12">Step</th>
                                                <th className="p-1.5">Marking Criteria</th>
                                                <th className="p-1.5 w-16 text-right">Marks</th>
                                              </tr>
                                            </thead>
                                            <tbody className="divide-y divide-emerald-200/60">
                                              {q.step_marking_rubric.map((r, sIdx) => (
                                                <tr key={sIdx}>
                                                  <td className="p-1.5 font-bold">{sIdx + 1}</td>
                                                  <td className="p-1.5">{r.rule}</td>
                                                  <td className="p-1.5 text-right font-bold">
                                                    {r.allocated_marks} M
                                                  </td>
                                                </tr>
                                              ))}
                                            </tbody>
                                          </table>
                                        </div>
                                      )}
                                    </div>
                                  )}
                                </div>

                                {/* Right Side: Marks & Swap Action */}
                                <div className="flex flex-col items-end space-y-2 flex-shrink-0">
                                  <span className="font-black text-sm text-slate-800 bg-slate-100 px-2.5 py-1 rounded-lg">
                                    [{q.marks} Mark{q.marks > 1 ? 's' : ''}]
                                  </span>

                                  <button
                                    onClick={() => handleSwap(q, secKey)}
                                    disabled={isSwapping}
                                    title="Swap with equivalent question matching syllabus & marks"
                                    className="flex items-center space-x-1 rounded-lg border border-slate-200 bg-white px-2.5 py-1.5 text-[11px] font-semibold text-slate-600 hover:border-blue-500 hover:text-blue-600 shadow-sm transition-all active:scale-95 disabled:opacity-50"
                                  >
                                    <RefreshCw className={`h-3 w-3 ${isSwapping ? 'animate-spin' : ''}`} />
                                    <span>Swap</span>
                                  </button>
                                </div>
                              </div>
                            </div>
                          );
                        })}
                      </div>
                    </div>
                  );
                })}
            </div>
          </div>
        </div>
      )}

      {/* Teacher Lead Capture Modal */}
      <LeadCaptureModal
        isOpen={isLeadModalOpen}
        onClose={() => setIsLeadModalOpen(false)}
        documentType={pendingDocDownload}
        examId={examPaper?.id}
        onSuccessDownload={() => {
          setIsUnlocked(true);
          triggerPdfDownload(pendingDocDownload);
        }}
      />
    </div>
  );
}
